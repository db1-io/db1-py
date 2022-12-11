"""Tests for item functions and API."""

import pytest
from utils import VALUE_LIST, compare_values

import db1


@pytest.fixture(params=VALUE_LIST)
def value(request):
    return request.param


def test_get_set(value):
    value = VALUE_LIST[value]
    key = "test_key"
    item = db1.Item(key)
    item.val = value
    ret_value = item.val
    item.delete()
    compare_values(value, ret_value)


def test_invalid_key():
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        db1.Item("-invalid_key-")
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        db1.Item("invalid_key@")
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        db1.Item("inval?d_key")
