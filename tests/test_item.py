"""Tests for item functions and API."""

# import threading
# import time
import uuid
from typing import Optional

import pytest
from utils import VALUE_LIST, compare_values

import db1


@pytest.fixture(params=VALUE_LIST)
def value(request):
    return request.param


def test_invalid_key():
    item = db1.Item("-invalid_key-")
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        item.set("test")

    item = db1.Item("invalid_key@")
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        item.set("test")

    item = db1.Item("inval?d_key")
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        item.set("test")

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        too_long_key = (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )
        db1.Item(too_long_key)

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        db1.Item("")


test_item: Optional[db1.Item] = None
test_key: str = str(uuid.uuid4())


def test_init():
    global test_item
    test_item = db1.Item(test_key)
    assert test_item.key == test_key


def test_set_get(value):
    value = VALUE_LIST[value]
    test_item.set(value)
    ret_value = test_item.get()
    compare_values(value, ret_value)


# def test_get_meta_variables():
#     meta_variables = test_item.meta_variables
#     keys = ["size_bytes", "created_ms", "updated_ms"]
#     assert all(key in meta_variables for key in keys)


def test_delete():
    test_item.delete()


def test_delete_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        test_item.delete()


def test_get_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        test_item.get()
