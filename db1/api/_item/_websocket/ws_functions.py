"""Item websocket API user interface functions."""

import json
from typing import Callable, Optional

from db1.api._item._rest.rest_functions import get_item
from db1.api._websocket_utils import make_ws_connection
from db1.api.environment_vars import DB1_API_ITEM_WEBSOCKET_URL
from db1.serializer._types import PY_TYPES_


def await_next_item(key: str) -> Optional[PY_TYPES_]:
    """Await next value of item.

    A very simple functions without any error handling.
    Use `listen` for more advanced use cases.

    Args:
        key: The key of the item.

    Returns:
        The new value of the item or None if the connection was closed or if an error occurred.

    Raises:
        db1.api._exceptions.NotFoundError: If the item does not exist.
        db1.api._exceptions.ItemValueTooBigError: If the item value is bigger than `max_size_bytes`.
    """
    value_set = False

    def on_message(ws, message):
        message = json.loads(message)
        if message["event_type"] == "set":
            nonlocal value_set
            value_set = True
            ws.close()

    make_ws_connection(
        DB1_API_ITEM_WEBSOCKET_URL,
        key,
        on_message=on_message,
    )
    if value_set:
        return get_item(key)

    return None


def listen(
    key: str,
    on_set_value: Optional[Callable[[PY_TYPES_], None]] = None,
    on_create: Optional[Callable[[], None]] = None,
    on_delete: Optional[Callable[[], None]] = None,
    on_open: Optional[Callable[[], None]] = None,
    on_error: Optional[Callable[[str], None]] = None,
    on_close: Optional[Callable[[str, str], None]] = None,
    enable_trace=False,
) -> None:
    """Listen for updates of an item value.

    Args:
        key: The key of the item.
        on_set_value: A callback that is called when the value of the item is set.
        on_create: A callback that is called when the item is created.
        on_delete: A callback that is called when the item is deleted.
        on_open: A callback that is called when the connection is opened.
        on_error: A callback that is called when an error occurs.
        on_close: A callback that is called when the connection is closed.
        enable_trace: Whether to enable trace logging.

    Raises:
        db1.api._exceptions.NotFoundError: If the item does not exist.
        db1.api._exceptions.ItemValueTooBigError: If the item value is bigger than `max_size_bytes`.
    """

    def _on_message(ws, message: str):
        message_dict = json.loads(message)
        if message_dict["event_type"] == "set":
            if on_set_value is not None:
                on_set_value(get_item(key))
        elif message_dict["event_type"] == "create":
            if on_create is not None:
                on_create()
        elif message_dict["event_type"] == "delete":
            if on_delete is not None:
                on_delete()

    def _on_error(ws, error: str):
        if on_error is not None:
            on_error(error)

    def _on_close(ws, close_status_code: str, close_msg: str):
        if on_close is not None:
            on_close(close_status_code, close_msg)

    def _on_open(ws):
        if on_open is not None:
            on_open()

    make_ws_connection(
        DB1_API_ITEM_WEBSOCKET_URL,
        key,
        on_message=_on_message,
        on_error=_on_error,
        on_close=_on_close,
        on_open=_on_open,
        enable_trace=enable_trace,
    )

    return
