"""Tests for serializer functions."""

import pytest
from utils import VALUE_LIST, compare_values

import db1


@pytest.fixture(params=VALUE_LIST)
def value(request):
    return request.param


def test(value):
    value = VALUE_LIST[value]
    ser_value = db1.serializer.dumps(value)
    ret_value = db1.serializer.loads(ser_value)
    compare_values(value, ret_value)
