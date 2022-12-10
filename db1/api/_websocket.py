"""Functions for handling websocket."""

import logging
from typing import Callable, Optional

import websocket


def make_ws_connection(
    url: str,
    resource_id: str,
    on_open: Optional[Callable[[websocket.WebSocketApp], None]] = None,
    on_message: Optional[Callable[[websocket.WebSocketApp, str], None]] = None,
    on_error: Optional[Callable[[websocket.WebSocketApp, str], None]] = None,
    on_close: Optional[Callable[[websocket.WebSocketApp, str, str], None]] = None,
    enable_trace=False,
):
    """Create websocket connection."""
    logging.info("Creating websocket connection")
    logging.debug(f"url: {url}, resource_id: {resource_id}")
    header = {"resource_id": resource_id}

    websocket.enableTrace(enable_trace)
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        header=header,
    )
    ws.run_forever()
