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

class Value(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            Value._Type.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NONE: Value._Type.ValueType  # 0
        INT64_: Value._Type.ValueType  # 1
        FLOAT_: Value._Type.ValueType  # 2
        STRING_: Value._Type.ValueType  # 3
        BOOL_: Value._Type.ValueType  # 4
        BYTES_: Value._Type.ValueType  # 5
        LIST: Value._Type.ValueType  # 6
        DICT: Value._Type.ValueType  # 7
        NDARRAY: Value._Type.ValueType  # 8
        DATAFRAME: Value._Type.ValueType  # 9

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    NONE: Value.Type.ValueType  # 0
    INT64_: Value.Type.ValueType  # 1
    FLOAT_: Value.Type.ValueType  # 2
    STRING_: Value.Type.ValueType  # 3
    BOOL_: Value.Type.ValueType  # 4
    BYTES_: Value.Type.ValueType  # 5
    LIST: Value.Type.ValueType  # 6
    DICT: Value.Type.ValueType  # 7
    NDARRAY: Value.Type.ValueType  # 8
    DATAFRAME: Value.Type.ValueType  # 9

    TYPE_FIELD_NUMBER: builtins.int
    INT64__FIELD_NUMBER: builtins.int
    FLOAT__FIELD_NUMBER: builtins.int
    STRING__FIELD_NUMBER: builtins.int
    BOOL__FIELD_NUMBER: builtins.int
    BYTES__FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    DICT_FIELD_NUMBER: builtins.int
    NDARRAY_FIELD_NUMBER: builtins.int
    DATA_FRAME_FIELD_NUMBER: builtins.int
    type: global___Value.Type.ValueType
    int64_: builtins.int
    float_: builtins.float
    string_: builtins.str
    bool_: builtins.bool
    bytes_: builtins.bytes
    @property
    def list(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Value
    ]: ...
    @property
    def dict(self) -> global___Dict: ...
    @property
    def ndarray(self) -> global___NDArray: ...
    @property
    def data_frame(self) -> global___DataFrame: ...
    def __init__(
        self,
        *,
        type: global___Value.Type.ValueType = ...,
        int64_: builtins.int = ...,
        float_: builtins.float = ...,
        string_: builtins.str = ...,
        bool_: builtins.bool = ...,
        bytes_: builtins.bytes = ...,
        list: collections.abc.Iterable[global___Value] | None = ...,
        dict: global___Dict | None = ...,
        ndarray: global___NDArray | None = ...,
        data_frame: global___DataFrame | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "data_frame", b"data_frame", "dict", b"dict", "ndarray", b"ndarray"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bool_",
            b"bool_",
            "bytes_",
            b"bytes_",
            "data_frame",
            b"data_frame",
            "dict",
            b"dict",
            "float_",
            b"float_",
            "int64_",
            b"int64_",
            "list",
            b"list",
            "ndarray",
            b"ndarray",
            "string_",
            b"string_",
            "type",
            b"type",
        ],
    ) -> None: ...

global___Value = Value

class NDArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BYTES__FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    bytes_: builtins.bytes
    @property
    def shape(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.int
    ]: ...
    type: builtins.str
    def __init__(
        self,
        *,
        bytes_: builtins.bytes = ...,
        shape: collections.abc.Iterable[builtins.int] | None = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bytes_", b"bytes_", "shape", b"shape", "type", b"type"
        ],
    ) -> None: ...

global___NDArray = NDArray

class Dict(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def keys(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]: ...
    @property
    def values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Value
    ]: ...
    def __init__(
        self,
        *,
        keys: collections.abc.Iterable[builtins.str] | None = ...,
        values: collections.abc.Iterable[global___Value] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["keys", b"keys", "values", b"values"],
    ) -> None: ...

global___Dict = Dict

class DataFrame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INDEX_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def index(self) -> global___Value: ...
    @property
    def columns(self) -> global___Value: ...
    @property
    def values(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Value
    ]: ...
    def __init__(
        self,
        *,
        index: global___Value | None = ...,
        columns: global___Value | None = ...,
        values: collections.abc.Iterable[global___Value] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["columns", b"columns", "index", b"index"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "columns", b"columns", "index", b"index", "values", b"values"
        ],
    ) -> None: ...

global___DataFrame = DataFrame
