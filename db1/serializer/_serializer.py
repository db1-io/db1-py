"""Serializer and deserializer functions."""

from db1._protos import SERIALIZER_PROTO_0v1 as pb
from db1.serializer._encoder import decode, encode
from db1.serializer._types import PY_TYPES_


def dumps(py_value: PY_TYPES_) -> bytes:
    """Serialize python value."""
    pb_value = encode(py_value)
    return pb_value.SerializeToString()


def loads(ser_value: bytes) -> PY_TYPES_:
    """Deserialize value."""
    pb_value = pb.Value.FromString(ser_value)
    return decode(pb_value)
