"""Item REST API low level functions."""

from typing import Optional, Tuple

from db1._protos import ITEM_PROTO_0v1 as pb
from db1.api import exceptions
from db1.api._http_utils import make_http_request
from db1.api._item._utils import check_common_status
from db1.api.environment_vars import (
    DB1_HTTP_DELETE_ENDPOINT,
    DB1_HTTP_GET_ENDPOINT,
    DB1_HTTP_SET_ENDPOINT,
)


def delete_request(resource_id: str):
    common_request = pb.CommonRequest()
    request = pb.DeleteRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_HTTP_DELETE_ENDPOINT, encoded_request)
    response = pb.DeleteResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.DeleteResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(f"An item with resource id `{resource_id}` does not exist.")
    if response.status == pb.DeleteResponse.Status.INVALID_RESOURCE_ID:
        raise exceptions.InvalidKeyError(f"The resource id `{resource_id}` is invalid.")
    if response.status == pb.DeleteResponse.Status.DELETED:
        pass

    return


def get_value_request(
    resource_id: str,
    max_size_bytes: Optional[int] = None,
) -> Tuple:
    common_request = pb.CommonRequest()
    request = pb.GetRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    request.without_metavaribles = True
    request.without_item_value = False
    if max_size_bytes is not None:
        request.max_size_bytes = max_size_bytes
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_HTTP_GET_ENDPOINT, encoded_request)
    response = pb.GetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.GetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(f"An item with resource id `{resource_id}` does not exist.")
    if response.status == pb.GetResponse.Status.FOUND:
        pass

    if response.size_bytes_bigger_than_max:
        raise exceptions.ItemValueTooBigError(
            f"The item value is bigger than the max size of {max_size_bytes} bytes."
        )

    return (
        response.item_value,
        response.size_bytes,
        response.created_ms,
        response.updated_ms,
    )


def set_value_request(resource_id: str, item_value: bytes) -> None:
    common_request = pb.CommonRequest()
    request = pb.SetRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    request.item_value = item_value
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_HTTP_SET_ENDPOINT, encoded_request)
    response = pb.SetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.SetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(f"An item with resource id `{resource_id}` does not exist.")
    if response.status == pb.SetResponse.Status.INVALID_RESOURCE_ID:
        raise exceptions.InvalidKeyError(f"Invalid resource id `{resource_id}`.")
    if response.status != pb.SetResponse.Status.UPDATED:
        pass

    return
