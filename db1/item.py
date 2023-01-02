"""Wrapper class for easy use of the Item API."""

from typing import Callable, Optional

from db1.api import item
from db1.api.item._utils import assert_valid_key, assert_public_key
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
            f"DB1 Item with key: `{self.key}`\n" f"Check it out at: {self.url}"
        )
        return repr_string

    def create(self) -> None:
        """Create the item.

        Raises:
            db1.api.exceptions.AlreadyExistsError: If the item already exists.
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        assert_public_key(key)
        item.create(self.key)

    def delete(self) -> None:
        """Delete the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        assert_public_key(key)
        item.delete(self.key)

    def get_value(self, max_size_bytes: Optional[int] = None) -> PY_TYPES_:
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
        return item.get_value(self.key, max_size_bytes=max_size_bytes)

    def set_value(self, value: PY_TYPES_) -> None:
        """Set the value of the item.

        Args:
            value: The value to set.
        
        Raises:
            db1.api.exceptions.InvalidKeyError: If the key is invalid.
        """
        assert_public_key(key)
        item.set_value(self.key, value)

    def get_meta_variables(self) -> dict:
        """Get the meta variables of the item.

        Returns:
            The meta variables of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
        """
        return item.get_meta_variables(self.key)

    def await_next_value(self) -> PY_TYPES_:
        """Wait for the next value of the item.

        Returns:
            The next value of the item.

        Raises:
            db1.api.exceptions.NotFoundError: If the item does not exist.
            db1.api.exceptions.ItemValueTooBigError:
                If the item value is bigger than `max_size_bytes`.
        """
        return item.await_next_value(self.key)

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
        item.listen(
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

    @property
    def val(self) -> PY_TYPES_:
        """Get the value of the item.

        See docstring of `item.get_value` for more information.
        """
        return self.get_value()

    @val.setter
    def val(self, value: PY_TYPES_) -> None:
        """Set the value of the item.

        See docstring of `item.set_value` for more information.
        """
        self.set_value(value)

    @property
    def meta_variables(self) -> dict:
        """Get the meta variables of the item.

        See docstring of `item.get_meta_variables` for more information.
        """
        return self.get_meta_variables()

    @property
    def next_val(self) -> PY_TYPES_:
        """Wait for the next value of the item.

        See docstring of `item.await_next_value` for more information.
        """
        return self.await_next_value()

    @property
    def url(self) -> str:
        """Get the URL of the item.

        See docstring of `item.get_url` for more information.
        """
        return self.get_url()

    @property
    def value(self) -> PY_TYPES_:
        """ "Not implemented, use Item.val instead."""
        raise NotImplementedError("Use Item.val instead.")

    @value.setter
    def value(self, value: PY_TYPES_) -> None:
        """ "Not implemented, use Item.val instead."""
        raise NotImplementedError("Use Item.val instead.")
