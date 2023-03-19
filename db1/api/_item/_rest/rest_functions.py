"""Item REST API user interface functions."""

from typing import Any, Dict, Optional, Tuple

from db1.api._item._rest.rest_requests import (
    delete_request,
    get_value_request,
    set_value_request,
)
from db1.api._item._utils import assert_valid_key, assert_valid_public_key
from db1.serializer._serializer import dumps, loads
from db1.serializer._types import PY_TYPES_


def delete_item(key: str) -> None:
    """Delete an item.

    Args:
        key: The key of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
        db1.api.exceptions.InvalidKeyError: If the key is invalid.
    """
    assert_valid_public_key(key)
    delete_request(key)


def get_item(key: str, max_size_bytes: Optional[int] = None) -> PY_TYPES_:
    """Get the value of an item.

    Args:
        key: The key of the item.
        max_size_bytes: The maximum size of the item value in bytes.

    Returns:
        The value of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
        db1.api.exceptions.ItemValueTooBigError: If the item value is bigger than `max_size_bytes`.
        db1.api.exceptions.InvalidKeyError: If the key is invalid.
    """
    assert_valid_key(key)
    item_value, _, _, _ = get_value_request(key, max_size_bytes)
    return loads(item_value)


def get_item_and_meta_variables(
    key: str,
    max_size_bytes: Optional[int] = None,
) -> Tuple[PY_TYPES_, Dict[str, Any]]:
    """Get the value and meta variables of an item.

    Args:
        key: The key of the item.
        max_size_bytes: The maximum size of the item value in bytes.

    Returns:
        The value and meta variables of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
        db1.api.exceptions.ItemValueTooBigError: If the item value is bigger than `max_size_bytes`.
        db1.api.exceptions.InvalidKeyError: If the key is invalid.
    """
    assert_valid_key(key)
    item_value, size_bytes, created_ms, updated_ms = get_value_request(key, max_size_bytes)
    meta_variables = {
        "size_bytes": size_bytes,
        "created_ms": created_ms,
        "updated_ms": updated_ms,
    }
    return loads(item_value), meta_variables


def set_item(key: str, value: PY_TYPES_) -> None:
    """Set the value of an item.

    Args:
        key: The key of the item.
        value: The value of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
        db1.api.exceptions.InvalidKeyError: If the key is invalid.
    """
    assert_valid_public_key(key)
    ser_value = dumps(value)
    set_value_request(key, ser_value)
