"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CommonRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    USAGE_CONTEXT_FIELD_NUMBER: builtins.int
    token: builtins.str
    usage_context: builtins.str
    def __init__(
        self,
        *,
        token: builtins.str = ...,
        usage_context: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "token", b"token", "usage_context", b"usage_context"
        ],
    ) -> None: ...

global___CommonRequest = CommonRequest

class CommonResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            CommonResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INTERNAL_ERROR: CommonResponse._Status.ValueType  # 0
        BAD_REQUEST: CommonResponse._Status.ValueType  # 1
        OK_REQUEST: CommonResponse._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    INTERNAL_ERROR: CommonResponse.Status.ValueType  # 0
    BAD_REQUEST: CommonResponse.Status.ValueType  # 1
    OK_REQUEST: CommonResponse.Status.ValueType  # 2

    MESSAGE_FIELD_NUMBER: builtins.int
    DEBUG_MESSAGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    message: builtins.str
    debug_message: builtins.str
    status: global___CommonResponse.Status.ValueType
    def __init__(
        self,
        *,
        message: builtins.str = ...,
        debug_message: builtins.str = ...,
        status: global___CommonResponse.Status.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "debug_message",
            b"debug_message",
            "message",
            b"message",
            "status",
            b"status",
        ],
    ) -> None: ...

global___CommonResponse = CommonResponse

class CreateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonRequest: ...
    resource_id: builtins.str
    def __init__(
        self,
        *,
        common: global___CommonRequest | None = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common", b"common", "resource_id", b"resource_id"
        ],
    ) -> None: ...

global___CreateRequest = CreateRequest

class CreateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            CreateResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ALREADY_EXISTS: CreateResponse._Status.ValueType  # 0
        CREATED: CreateResponse._Status.ValueType  # 1
        INVALID_RESOURCE_ID: CreateResponse._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    ALREADY_EXISTS: CreateResponse.Status.ValueType  # 0
    CREATED: CreateResponse.Status.ValueType  # 1
    INVALID_RESOURCE_ID: CreateResponse.Status.ValueType  # 2

    COMMON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonResponse: ...
    status: global___CreateResponse.Status.ValueType
    def __init__(
        self,
        *,
        common: global___CommonResponse | None = ...,
        status: global___CreateResponse.Status.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["common", b"common", "status", b"status"],
    ) -> None: ...

global___CreateResponse = CreateResponse

class GetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    WITHOUT_METAVARIBLES_FIELD_NUMBER: builtins.int
    WITHOUT_ITEM_VALUE_FIELD_NUMBER: builtins.int
    MAX_SIZE_BYTES_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonRequest: ...
    resource_id: builtins.str
    without_metavaribles: builtins.bool
    without_item_value: builtins.bool
    max_size_bytes: builtins.int
    def __init__(
        self,
        *,
        common: global___CommonRequest | None = ...,
        resource_id: builtins.str = ...,
        without_metavaribles: builtins.bool = ...,
        without_item_value: builtins.bool = ...,
        max_size_bytes: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common",
            b"common",
            "max_size_bytes",
            b"max_size_bytes",
            "resource_id",
            b"resource_id",
            "without_item_value",
            b"without_item_value",
            "without_metavaribles",
            b"without_metavaribles",
        ],
    ) -> None: ...

global___GetRequest = GetRequest

class GetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            GetResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NOT_FOUND: GetResponse._Status.ValueType  # 0
        FOUND: GetResponse._Status.ValueType  # 1

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    NOT_FOUND: GetResponse.Status.ValueType  # 0
    FOUND: GetResponse.Status.ValueType  # 1

    class Metavarible(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    COMMON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ITEM_VALUE_FIELD_NUMBER: builtins.int
    METAVARIBLES_FIELD_NUMBER: builtins.int
    SIZE_BYTES_BIGGER_THAN_MAX_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    CREATED_MS_FIELD_NUMBER: builtins.int
    UPDATED_MS_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonResponse: ...
    status: global___GetResponse.Status.ValueType
    item_value: builtins.bytes
    @property
    def metavaribles(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___GetResponse.Metavarible
    ]: ...
    size_bytes_bigger_than_max: builtins.bool
    size_bytes: builtins.int
    created_ms: builtins.int
    updated_ms: builtins.int
    def __init__(
        self,
        *,
        common: global___CommonResponse | None = ...,
        status: global___GetResponse.Status.ValueType = ...,
        item_value: builtins.bytes = ...,
        metavaribles: collections.abc.Iterable[global___GetResponse.Metavarible]
        | None = ...,
        size_bytes_bigger_than_max: builtins.bool = ...,
        size_bytes: builtins.int = ...,
        created_ms: builtins.int = ...,
        updated_ms: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common",
            b"common",
            "created_ms",
            b"created_ms",
            "item_value",
            b"item_value",
            "metavaribles",
            b"metavaribles",
            "size_bytes",
            b"size_bytes",
            "size_bytes_bigger_than_max",
            b"size_bytes_bigger_than_max",
            "status",
            b"status",
            "updated_ms",
            b"updated_ms",
        ],
    ) -> None: ...

global___GetResponse = GetResponse

class SetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    ITEM_VALUE_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonRequest: ...
    resource_id: builtins.str
    item_value: builtins.bytes
    def __init__(
        self,
        *,
        common: global___CommonRequest | None = ...,
        resource_id: builtins.str = ...,
        item_value: builtins.bytes = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common",
            b"common",
            "item_value",
            b"item_value",
            "resource_id",
            b"resource_id",
        ],
    ) -> None: ...

global___SetRequest = SetRequest

class SetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            SetResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NOT_FOUND: SetResponse._Status.ValueType  # 0
        UPDATED: SetResponse._Status.ValueType  # 1
        INVALID_RESOURCE_ID: SetResponse._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    NOT_FOUND: SetResponse.Status.ValueType  # 0
    UPDATED: SetResponse.Status.ValueType  # 1
    INVALID_RESOURCE_ID: SetResponse.Status.ValueType  # 2

    COMMON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonResponse: ...
    status: global___SetResponse.Status.ValueType
    def __init__(
        self,
        *,
        common: global___CommonResponse | None = ...,
        status: global___SetResponse.Status.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["common", b"common", "status", b"status"],
    ) -> None: ...

global___SetResponse = SetResponse

class UpdateMetavariblesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Metavarible(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        DELETE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        delete: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
            delete: builtins.bool = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "delete", b"delete", "key", b"key", "value", b"value"
            ],
        ) -> None: ...

    COMMON_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    METAVARIBLES_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonRequest: ...
    resource_id: builtins.str
    @property
    def metavaribles(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___UpdateMetavariblesRequest.Metavarible
    ]: ...
    def __init__(
        self,
        *,
        common: global___CommonRequest | None = ...,
        resource_id: builtins.str = ...,
        metavaribles: collections.abc.Iterable[
            global___UpdateMetavariblesRequest.Metavarible
        ]
        | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common",
            b"common",
            "metavaribles",
            b"metavaribles",
            "resource_id",
            b"resource_id",
        ],
    ) -> None: ...

global___UpdateMetavariblesRequest = UpdateMetavariblesRequest

class UpdateMetavariblesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            UpdateMetavariblesResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NOT_FOUND: UpdateMetavariblesResponse._Status.ValueType  # 0
        UPDATED: UpdateMetavariblesResponse._Status.ValueType  # 1
        INVALID_RESOURCE_ID: UpdateMetavariblesResponse._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    NOT_FOUND: UpdateMetavariblesResponse.Status.ValueType  # 0
    UPDATED: UpdateMetavariblesResponse.Status.ValueType  # 1
    INVALID_RESOURCE_ID: UpdateMetavariblesResponse.Status.ValueType  # 2

    COMMON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonResponse: ...
    status: global___UpdateMetavariblesResponse.Status.ValueType
    def __init__(
        self,
        *,
        common: global___CommonResponse | None = ...,
        status: global___UpdateMetavariblesResponse.Status.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["common", b"common", "status", b"status"],
    ) -> None: ...

global___UpdateMetavariblesResponse = UpdateMetavariblesResponse

class DeleteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonRequest: ...
    resource_id: builtins.str
    def __init__(
        self,
        *,
        common: global___CommonRequest | None = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "common", b"common", "resource_id", b"resource_id"
        ],
    ) -> None: ...

global___DeleteRequest = DeleteRequest

class DeleteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            DeleteResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NOT_FOUND: DeleteResponse._Status.ValueType  # 0
        DELETED: DeleteResponse._Status.ValueType  # 1
        INVALID_RESOURCE_ID: DeleteResponse._Status.ValueType  # 2

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    NOT_FOUND: DeleteResponse.Status.ValueType  # 0
    DELETED: DeleteResponse.Status.ValueType  # 1
    INVALID_RESOURCE_ID: DeleteResponse.Status.ValueType  # 2

    COMMON_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonResponse: ...
    status: global___DeleteResponse.Status.ValueType
    def __init__(
        self,
        *,
        common: global___CommonResponse | None = ...,
        status: global___DeleteResponse.Status.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["common", b"common"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["common", b"common", "status", b"status"],
    ) -> None: ...

global___DeleteResponse = DeleteResponse

class SubscribeToItemWSRequest(google.protobuf.message.Message):
    """Web socket stuff"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    request_id: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "request_id", b"request_id", "resource_id", b"resource_id"
        ],
    ) -> None: ...

global___SubscribeToItemWSRequest = SubscribeToItemWSRequest

class SubscribeToItemWSResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            SubscribeToItemWSResponse._Status.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NOT_FOUND: SubscribeToItemWSResponse._Status.ValueType  # 0
        SUBSCRIBED: SubscribeToItemWSResponse._Status.ValueType  # 1

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    NOT_FOUND: SubscribeToItemWSResponse.Status.ValueType  # 0
    SUBSCRIBED: SubscribeToItemWSResponse.Status.ValueType  # 1

    STATUS_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    status: global___SubscribeToItemWSResponse.Status.ValueType
    request_id: builtins.str
    def __init__(
        self,
        *,
        status: global___SubscribeToItemWSResponse.Status.ValueType = ...,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "request_id", b"request_id", "status", b"status"
        ],
    ) -> None: ...

global___SubscribeToItemWSResponse = SubscribeToItemWSResponse

class ItemEventWSPush(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EventType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EventTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ItemEventWSPush._EventType.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CREATED: ItemEventWSPush._EventType.ValueType  # 0
        UPDATED: ItemEventWSPush._EventType.ValueType  # 1
        DELETED: ItemEventWSPush._EventType.ValueType  # 2

    class EventType(_EventType, metaclass=_EventTypeEnumTypeWrapper): ...
    CREATED: ItemEventWSPush.EventType.ValueType  # 0
    UPDATED: ItemEventWSPush.EventType.ValueType  # 1
    DELETED: ItemEventWSPush.EventType.ValueType  # 2

    RESOURCE_ID_FIELD_NUMBER: builtins.int
    resource_id: builtins.str
    def __init__(
        self,
        *,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_id", b"resource_id"]
    ) -> None: ...

global___ItemEventWSPush = ItemEventWSPush
