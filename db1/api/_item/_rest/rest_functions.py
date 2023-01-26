"""Item REST API user interface functions."""

from typing import Any, Dict, List, Optional, Tuple

from db1.api import exceptions
from db1.api._item._rest.rest_requests import (
    create_request,
    delete_meta_variables_request,
    delete_request,
    get_meta_variables_request,
    get_value_and_meta_variables_request,
    get_value_request,
    set_value_request,
    update_meta_variables_request,
)
from db1.serializer._serializer import dumps, loads
from db1.serializer._types import PY_TYPES_


def _create_item(key: str) -> None:
    """Create an item.

    Args:
        key: The key of the item.

    Raises:
        db1.api.exceptions.AlreadyExistsError: If the item already exists.
    """
    create_request(key)


def delete_item(key: str) -> None:
    """Delete an item.

    Args:
        key: The key of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
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
    """
    item_value, _, _, _ = get_value_request(key, max_size_bytes)
    return loads(item_value)


def get_item_meta_variables(
    key: str,
) -> Dict:
    """Get the meta variables of an item.

    Args:
        key: The key of the item.

    Returns:
        The meta variables of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    _meta_variables, size_bytes, created_ms, updated_ms = get_meta_variables_request(
        key
    )

    meta_variables = {
        "size_bytes": size_bytes,
        "created_ms": created_ms,
        "updated_ms": updated_ms,
        **{meta_variable.key: meta_variable.value for meta_variable in _meta_variables},
    }
    return meta_variables


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
    """
    (
        item_value,
        _meta_variables,
        size_bytes,
        created_ms,
        updated_ms,
    ) = get_value_and_meta_variables_request(key, max_size_bytes)

    meta_variables = {
        "size_bytes": size_bytes,
        "created_ms": created_ms,
        "updated_ms": updated_ms,
        **{meta_variable.key: meta_variable.value for meta_variable in _meta_variables},
    }
    return item_value, meta_variables


def set_item(key: str, value: PY_TYPES_) -> None:
    """Set the value of an item.

    Args:
        key: The key of the item.
        value: The value of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    ser_value = dumps(value)
    try:
        set_value_request(key, ser_value)
    except exceptions.NotFoundError:
        _create_item(key)
        set_value_request(key, ser_value)


def update_item_meta_variables(
    key: str,
    meta_variables: Dict[str, str],
) -> None:
    """Update the meta variables of an item.

    Args:
        key: The key of the item.
        meta_variables: The meta variables of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    update_meta_variables_request(key, meta_variables)


def delete_item_meta_variables(
    key: str,
    meta_variable_keys: List[str],
) -> None:
    """Delete the meta variables of an item.

    Args:
        key: The key of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    delete_meta_variables_request(key, meta_variable_keys)
