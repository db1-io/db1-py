"""Wrapper class for easy use of the Item API."""

from typing import Callable, Optional

from db1.api import _item
from db1.api._item._utils import assert_valid_key
from db1.serializer._types import PY_TYPES_


class Item:
    def __init__(self, key: str):
        """Create an Item object.

        Args:
            key: The key of the item.

        Raises:
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        assert_valid_key(key)
        self.key = key

    def __repr__(self) -> str:
        repr_string = (
            f"DB1 Item with key: `{self.key}`\n" f"Check it out at: {self.get_url()}"
        )
        return repr_string

    def delete(self) -> None:
        """Delete the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
        """
        _item.delete_item(self.key)

    def get(self, max_size_bytes: Optional[int] = None) -> PY_TYPES_:
        """Get the value of the item.

        Args:
            max_size_bytes: The maximum size of the item value in bytes.
                If the item value is bigger than this, an error is raised.

        Returns:
            The value of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.ItemValueTooBigError:
                If the item value is bigger than `max_size_bytes`.
        """
        return _item.get_item(self.key, max_size_bytes=max_size_bytes)

    def set(self, value: PY_TYPES_) -> None:
        """Set the value of the item.

        Args:
            value: The value to set.
        """
        _item.set_item(self.key, value)

    def await_next(self) -> PY_TYPES_:
        """Wait for the next value of the item.

        Returns:
            The next value of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.ItemValueTooBigError:
                If the item value is bigger than `max_size_bytes`.
        """
        return _item.await_next_item(self.key)

    def listen(
        self,
        on_set_value: Optional[Callable[[PY_TYPES_], None]] = None,
        on_create: Optional[Callable[[], None]] = None,
        on_delete: Optional[Callable[[], None]] = None,
        on_open: Optional[Callable[[], None]] = None,
        on_error: Optional[Callable[[str], None]] = None,
        on_close: Optional[Callable[[str, str], None]] = None,
        enable_trace=False,
    ) -> None:
        """Listen for updates of the item value.

        Args:
            on_set_value: A callback that is called when the value of the item is set.
            on_create: A callback that is called when the item is created.
            on_delete: A callback that is called when the item is deleted.
            on_open: A callback that is called when the connection is opened.
            on_error: A callback that is called when an error occurs.
            on_close: A callback that is called when the connection is closed.
            enable_trace: Whether to enable trace logging.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.ItemValueTooBigError:
                If the item value is bigger than `max_size_bytes`.
        """
        _item.listen(
            self.key,
            on_set_value=on_set_value,
            on_create=on_create,
            on_delete=on_delete,
            on_open=on_open,
            on_error=on_error,
            on_close=on_close,
            enable_trace=enable_trace,
        )

    def get_url(self) -> str:
        """Get the URL of the item.

        Returns:
            The URL of the item.
        """
        return f"https://panel.db1.io/?key={self.key}"
