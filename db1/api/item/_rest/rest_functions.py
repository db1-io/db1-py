"""Item REST API user interface functions."""

from typing import Any, Dict, List, Optional, Tuple

from db1.api import exceptions
from db1.api.item._rest.rest_requests import (
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


def create(resource_id: str) -> None:
    """Create an item.

    Args:
        resource_id: The resource ID of the item.

    Raises:
        db1.api.exceptions.AlreadyExistsError: If the item already exists.
    """
    create_request(resource_id)


def delete(resource_id: str) -> None:
    """Delete an item.

    Args:
        resource_id: The resource ID of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    delete_request(resource_id)


def get_value(resource_id: str, max_size_bytes: Optional[int] = None) -> PY_TYPES_:
    """Get the value of an item.

    Args:
        resource_id: The resource ID of the item.
        max_size_bytes: The maximum size of the item value in bytes.

    Returns:
        The value of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
        db1.api.exceptions.ItemValueTooBigError: If the item value is bigger than `max_size_bytes`.
    """
    item_value, _, _, _ = get_value_request(resource_id, max_size_bytes)
    return loads(item_value)


def get_meta_variables(
    resource_id: str,
) -> Dict:
    """Get the meta variables of an item.

    Args:
        resource_id: The resource ID of the item.

    Returns:
        The meta variables of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    _meta_variables, size_bytes, created_ms, updated_ms = get_meta_variables_request(
        resource_id
    )

    meta_variables = {
        "size_bytes": size_bytes,
        "created_ms": created_ms,
        "updated_ms": updated_ms,
        **{meta_variable.key: meta_variable.value for meta_variable in _meta_variables},
    }
    return meta_variables


def get_value_and_meta_variables(
    resource_id: str,
    max_size_bytes: Optional[int] = None,
) -> Tuple[PY_TYPES_, Dict[str, Any]]:
    """Get the value and meta variables of an item.

    Args:
        resource_id: The resource ID of the item.
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
    ) = get_value_and_meta_variables_request(resource_id, max_size_bytes)

    meta_variables = {
        "size_bytes": size_bytes,
        "created_ms": created_ms,
        "updated_ms": updated_ms,
        **{meta_variable.key: meta_variable.value for meta_variable in _meta_variables},
    }
    return item_value, meta_variables


def set_value(resource_id: str, value: PY_TYPES_) -> None:
    """Set the value of an item.

    Args:
        resource_id: The resource ID of the item.
        value: The value of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    ser_value = dumps(value)
    try:
        set_value_request(resource_id, ser_value)
    except exceptions.NotFoundError:
        create(resource_id)
        set_value_request(resource_id, ser_value)


def update_meta_variables(
    resource_id: str,
    meta_variables: Dict[str, str],
) -> None:
    """Update the meta variables of an item.

    Args:
        resource_id: The resource ID of the item.
        meta_variables: The meta variables of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    update_meta_variables_request(resource_id, meta_variables)


def delete_meta_variables(
    resource_id: str,
    meta_variable_keys: List[str],
) -> None:
    """Delete the meta variables of an item.

    Args:
        resource_id: The resource ID of the item.

    Raises:
        db1.api.exceptions.NotFoundError: If the item does not exist.
    """
    delete_meta_variables_request(resource_id, meta_variable_keys)
