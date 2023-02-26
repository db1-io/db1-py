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


# def test_next_value():
#     test_value = "test_value"

#     def sleep_set_value(name):
#         time.sleep(0.5)
#         test_item.val = test_value

#     set_value_thread = threading.Thread(target=sleep_set_value, args=(1,))
#     set_value_thread.start()
#     time.sleep(0.2)
#     ret_value = test_item.next_val
#     time.sleep(0.2)
#     set_value_thread.join()
#     assert ret_value == test_value


# def test_listen():
#     local_test_key = str(uuid.uuid4())
#     test_value = "test_value"
#     local_test_item = db1.Item(local_test_key)

#     set_run = False
#     create_run = False
#     delete_run = False
#     open_run = False
#     close_run = False

#     def sleep_set_value(name):
#         time.sleep(0.5)
#         print(1)
#         local_test_item.create()
#         time.sleep(0.2)
#         print(2)
#         local_test_item.val = test_value
#         time.sleep(0.2)
#         print(3)
#         local_test_item.delete()


#     set_value_thread = threading.Thread(target=sleep_set_value, args=(1,))
#     set_value_thread.start()
#     time.sleep(0.1)

#     def on_set_value(value):
#         print("set")
#         global set_run
#         set_run = True
#         assert value == test_value

#     def on_create():
#         print("create")
#         global create_run
#         create_run = True

#     def on_delete():
#         print("delete")
#         global delete_run
#         delete_run = True

#     def on_open():
#         print("open")
#         global open_run
#         open_run = True

#     def on_close(a, b):
#         print(a)
#         print(b)
#         global close_run
#         close_run = True
#     print(100)
#     print(set_run)
#     local_test_item.listen(
#         on_set_value=on_set_value,
#         on_create=on_create,
#         on_delete=on_delete,
#         on_open=on_open,
#         on_close=on_close
#     )
#     print(111)
#     print(set_run)
#     set_value_thread.join()

#     assert set_run
#     assert create_run
#     assert delete_run
#     assert open_run
#     assert close_run


def test_delete():
    test_item.delete()


def test_delete_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        test_item.delete()


def test_get_not_found():
    with pytest.raises(db1.api.exceptions.NotFoundError):
        test_item.get()
