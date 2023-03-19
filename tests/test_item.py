"""Tests for item functions and API."""

import uuid

import pytest
from utils import VALUE_LIST, compare_values

import db1
from db1 import DB1


@pytest.fixture(params=VALUE_LIST)
def value(request):
    return request.param


def test_invalid_key():
    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        DB1["-invalid_key-"] = "test"

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        DB1["invalid_key@"] = "test"

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        DB1["inval?d_key"] = "test"

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        too_long_key = (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        )
        DB1[too_long_key]

    with pytest.raises(db1.api.exceptions.InvalidKeyError):
        DB1[""]


test_key: str = str(uuid.uuid4())


def test_get_url():
    url = db1.get_url(test_key)
    assert url == f"{db1.api.environment_vars.DB1_PANEL_URL}/?key={test_key}"


def test_serializer(value):
    value = VALUE_LIST[value]
    ser_value = db1.serializer.dumps(value)
    ret_value = db1.serializer.loads(ser_value)
    compare_values(value, ret_value)


def test_client():
    test_value = "test"
    DB1[test_key] = test_value
    ret_value = DB1[test_key]
    compare_values(test_value, ret_value)
    del DB1[test_key]
    repr(DB1)


def test_get_item_and_meta_variables():
    test_value = "test"
    DB1[test_key] = test_value
    ret_value, meta_variables = db1.get_item_and_meta_variables(test_key)
    compare_values(test_value, ret_value)
    assert all(key in meta_variables for key in ["size_bytes", "created_ms", "updated_ms"])
    assert type(meta_variables["size_bytes"]) == int
    assert type(meta_variables["created_ms"]) == int
    assert type(meta_variables["updated_ms"]) == int
    del DB1[test_key]


def test_set_get(value):
    value = VALUE_LIST[value]
    db1.set_item(test_key, value)
    ret_value = db1.get_item(test_key)
    compare_values(value, ret_value)


def test_delete():
    db1.delete_item(test_key)


def test_delete_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        db1.delete_item(test_key)
    with pytest.raises(db1.api.exceptions.NotFoundError):
        del DB1[test_key]


def test_get_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        db1.get_item(test_key)
    with pytest.raises(db1.api.exceptions.NotFoundError):
        DB1[test_key]
