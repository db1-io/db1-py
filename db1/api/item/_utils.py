"""Utility functions for Item API."""

from db1._protos import ITEM_PROTO_0v1 as pb
from db1.api import exceptions


def check_common_status(status: int):
    if status == pb.CommonResponse.Status.INTERNAL_ERROR:
        raise exceptions.InternalServerError("An internal error occured on the server.")
    if status == pb.CommonResponse.Status.BAD_REQUEST:
        raise exceptions.InternalServerError("The server received a bad request.")
    if status == pb.CommonResponse.Status.OK_REQUEST:
        return
