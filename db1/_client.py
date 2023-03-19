"""Wrapper class for easy use of the Item API."""

from typing import Optional

from db1.api._item import delete_item, get_item, set_item
from db1.serializer._types import PY_TYPES_


class DB1_:
    """DB1 object.

    Attributes:
        max_size_bytes: The maximum size of an item value in bytes on get.
    """

    max_size_bytes: Optional[int]

    def __repr__(self) -> str:
        return (
            "A global Python dict in the cloud.\n\n"
            "View the items in your browser at https://db1.io\n"
            "Read the documentation at "
            "https://db1-io.notion.site/DB1-Documentation-f5942d3984f7456ca49fba70c971bbf6"
        )

    def __init__(self):
        """Create a DB1 object."""
        self.max_size_bytes = None

    def __getitem__(self, key: str):
        """Get the value of an item.

        Args:
            key: The key of the item.

        Returns:
            The value of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.ItemValueTooBigError:
                If the item value is bigger than `max_size_bytes`.
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        return get_item(key, max_size_bytes=self.max_size_bytes)

    def __setitem__(self, key: str, value: PY_TYPES_):
        """Set the value of an item.

        Args:
            key: The key of the item.
            value: The value of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        set_item(key, value)

    def __delitem__(self, key: str):
        """Delete an item.

        Args:
            key: The key of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        delete_item(key)


DB1 = DB1_()
"""DB1 object."""
