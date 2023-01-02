"""Utility functions for Item API."""

from db1._protos import ITEM_PROTO_0v1 as pb
from db1.api import exceptions


def check_common_status(status: int, message: str):
    if status == pb.CommonResponse.Status.INTERNAL_ERROR:
        raise exceptions.InternalServerError(message)
    if status == pb.CommonResponse.Status.BAD_REQUEST:
        raise exceptions.InternalServerError(message)
    if status == pb.CommonResponse.Status.OK_REQUEST:
        return


def assert_valid_key(key: str) -> None:
    # Check if key is empty
    if not key:
        raise exceptions.InvalidKeyError("key is empty.")

    # Check if key is more than 100 characters
    if len(key) > 100:
        raise exceptions.InvalidKeyError("key is more than 100 characters.")


def assert_public_key(key: str) -> None:
    # Check if key dont starts with a letter or number
    if not key[0].isalnum():
        raise exceptions.InvalidKeyError("Public key must start with a letter or number.")

    # Check if key only contains letters, numbers, -, _
    if not all(char.isalnum() or char in "-_" for char in key):
        raise exceptions.InvalidKeyError(
            "Public key must contain only letters, numbers, '-' or '_'."
        )