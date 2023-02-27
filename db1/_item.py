"""Wrapper class for easy use of the Item API."""

from typing import Optional

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

    def get_url(self) -> str:
        """Get the URL of the item.

        Returns:
            The URL of the item.
        """
        return f"https://panel.db1.io/?key={self.key}"
