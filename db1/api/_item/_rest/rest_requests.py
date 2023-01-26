"""Item REST API low level functions."""

from typing import Dict, List, Optional, Tuple

from db1._protos import ITEM_PROTO_0v1 as pb
from db1.api import exceptions
from db1.api._http_utils import make_http_request
from db1.api._item._utils import check_common_status
from db1.api.environment_vars import (
    DB1_API_ITEM_CREATE_URL,
    DB1_API_ITEM_DELETE_URL,
    DB1_API_ITEM_GET_URL,
    DB1_API_ITEM_SET_URL,
)


def create_request(resource_id: str):
    common_request = pb.CommonRequest()
    request = pb.CreateRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_CREATE_URL, encoded_request)
    response = pb.CreateResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.CreateResponse.Status.ALREADY_EXISTS:
        raise exceptions.AlreadyExistsError(
            f"An item with resource id `{resource_id}` already exists."
        )
    if response.status == pb.CreateResponse.Status.INVALID_RESOURCE_ID:
        raise exceptions.InvalidKeyError(f"The resource id `{resource_id}` is invalid.")
    if response.status == pb.CreateResponse.Status.CREATED:
        pass


def delete_request(resource_id: str):
    common_request = pb.CommonRequest()
    request = pb.DeleteRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_DELETE_URL, encoded_request)
    response = pb.DeleteResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.DeleteResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
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

    http_response = make_http_request(DB1_API_ITEM_GET_URL, encoded_request)
    response = pb.GetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.GetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
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


def get_meta_variables_request(resource_id: str) -> Tuple:
    common_request = pb.CommonRequest()
    request = pb.GetRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    request.without_metavaribles = False
    request.without_item_value = True
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_GET_URL, encoded_request)
    response = pb.GetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.GetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
    if response.status == pb.GetResponse.Status.FOUND:
        pass

    return (
        response.metavaribles,
        response.size_bytes,
        response.created_ms,
        response.updated_ms,
    )


def get_value_and_meta_variables_request(
    resource_id: str,
    max_size_bytes: Optional[int] = None,
) -> Tuple:
    common_request = pb.CommonRequest()
    request = pb.GetRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    request.without_metavaribles = False
    request.without_item_value = False
    if max_size_bytes is not None:
        request.max_size_bytes = max_size_bytes
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_GET_URL, encoded_request)
    response = pb.GetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.GetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
    if response.status == pb.GetResponse.Status.FOUND:
        pass

    if response.size_bytes_bigger_than_max:
        raise exceptions.ItemValueTooBigError(
            f"The item value is bigger than the max size of {max_size_bytes} bytes."
        )

    return (
        response.item_value,
        response.metavaribles,
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

    http_response = make_http_request(DB1_API_ITEM_SET_URL, encoded_request)
    response = pb.SetResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.SetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
    if response.status == pb.SetResponse.Status.INVALID_RESOURCE_ID:
        raise exceptions.InvalidKeyError(f"Invalid resource id `{resource_id}`.")
    if response.status != pb.SetResponse.Status.UPDATED:
        pass

    return


def update_meta_variables_request(
    resource_id: str, metavariables: Dict[str, str]
) -> None:
    common_request = pb.CommonRequest()
    request = pb.UpdateMetavariblesRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    for key, value in metavariables.items():
        metavarible = pb.UpdateMetavariblesRequest.Metavarible()
        metavarible.key = key
        metavarible.value = value
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_SET_URL, encoded_request)
    response = pb.UpdateMetavariblesResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.SetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
    if response.status == pb.SetResponse.Status.INVALID_RESOURCE_ID:
        raise exceptions.InvalidKeyError(f"Invalid resource id `{resource_id}`.")
    if response.status == pb.SetResponse.Status.UPDATED:
        pass

    return


def delete_meta_variables_request(
    resource_id: str, meta_variable_keys: List[str]
) -> None:
    common_request = pb.CommonRequest()
    request = pb.UpdateMetavariblesRequest()
    request.common.CopyFrom(common_request)
    request.resource_id = resource_id
    for key in meta_variable_keys:
        metavarible = pb.UpdateMetavariblesRequest.Metavarible()
        metavarible.key = key
        metavarible.delete = True
    encoded_request = request.SerializeToString()

    http_response = make_http_request(DB1_API_ITEM_SET_URL, encoded_request)
    response = pb.UpdateMetavariblesResponse()
    response.ParseFromString(http_response.content)

    check_common_status(response.common.status, response.common.message)

    if response.status == pb.SetResponse.Status.NOT_FOUND:
        raise exceptions.NotFoundError(
            f"An item with resource id `{resource_id}` does not exist."
        )
    if response.status == pb.SetResponse.Status.UPDATED:
        pass

    return
