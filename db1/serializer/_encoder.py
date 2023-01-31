"""Encoder and decoder functions."""

from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd
import pyarrow as pa

from db1._protos import SERIALIZER_PROTO_0v1 as pb
from db1.serializer._types import PY_TYPES, PY_TYPES_


def _encode_int(py_value: int) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.INT64_
    pb_value.int64_ = py_value
    return pb_value


def _decode_int(pb_value: pb.Value) -> int:
    py_value = pb_value.int64_
    return py_value


def _encode_float(py_value: float) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.FLOAT_
    pb_value.float_ = py_value
    return pb_value


def _decode_float(pb_value: pb.Value) -> float:
    py_value = pb_value.float_
    return py_value


def _encode_string(py_value: str) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.STRING_
    pb_value.string_ = py_value
    return pb_value


def _decode_string(pb_value: pb.Value) -> str:
    py_value = pb_value.string_
    return py_value


def _encode_bool(py_value: bool) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.BOOL_
    pb_value.bool_ = py_value
    return pb_value


def _decode_bool(pb_value: pb.Value) -> bool:
    py_value = pb_value.bool_
    return py_value


def _encode_bytes(py_value: bytes) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.Type.BYTES_
    pb_value.bytes_ = py_value
    return pb_value


def _decode_bytes(pb_value: pb.Value) -> bytes:
    py_value = pb_value.bytes_
    return py_value


def _encode_list(py_value: List) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.LIST
    for sub_value in py_value:
        pb_value.list.extend([encode(sub_value)])
    return pb_value


def _decode_list(pb_value: pb.Value) -> List:
    py_value = []
    for sub_value in pb_value.list:
        py_value.append(decode(sub_value))
    return py_value


def _encode_dict(py_value: Dict[str, PY_TYPES_]) -> pb.Value:
    assert "__value_type__" not in py_value, "Illegal key."
    pb_value = pb.Value()
    pb_value.type = pb.Value.DICT
    dict_ = pb.Dict()
    for key in py_value:
        assert type(key) == str, f"Type of key '{key}' is not string."
        dict_.keys.extend([key])
        dict_.values.extend([encode(py_value[key])])
    pb_value.dict.CopyFrom(dict_)
    return pb_value


def _decode_dict(pb_value: pb.Value) -> Dict[str, PY_TYPES_]:
    py_value = {}
    assert len(pb_value.dict.keys) == len(pb_value.dict.values)
    for i in range(len(pb_value.dict.keys)):
        py_value[pb_value.dict.keys[i]] = decode(pb_value.dict.values[i])
    return py_value


def _encode_ndarray(py_value: np.ndarray) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.NDARRAY
    ndarray = pb.NDArray()
    ndarray.bytes_ = py_value.tobytes()
    ndarray.shape[:] = py_value.shape
    ndarray.type = str(py_value.dtype)
    pb_value.ndarray.CopyFrom(ndarray)
    return pb_value


def _decode_ndarray(pb_value: pb.Value) -> np.ndarray:
    py_value = np.frombuffer(pb_value.ndarray.bytes_, dtype=pb_value.ndarray.type)
    py_value = py_value.reshape(pb_value.ndarray.shape)
    return py_value


def _encode_dataframe(py_value: pd.DataFrame) -> pb.Value:
    pb_value = pb.Value()
    pb_value.type = pb.Value.DATAFRAME
    table = pa.Table.from_pandas(py_value)
    batches = table.to_batches()
    batch = batches[0]
    sink = pa.BufferOutputStream()
    with pa.ipc.new_stream(sink, batch.schema) as writer:
        writer.write_batch(batch)
    buf = sink.getvalue()
    pb_value.bytes_ = buf.to_pybytes()
    return pb_value


def _decode_dataframe(pb_value: pb.Value) -> pd.DataFrame:
    buf = pa.py_buffer(pb_value.bytes_)
    with pa.ipc.open_stream(buf) as reader:
        py_value = reader.read_pandas()
    return py_value


_ENCODERS: List[Callable[[Any], pb.Value]] = [
    _encode_int,
    _encode_float,
    _encode_string,
    _encode_bool,
    _encode_bytes,
    _encode_list,
    _encode_dict,
    _encode_ndarray,
    _encode_dataframe,
]


_DECODERS: List[Callable[[pb.Value], Any]] = [
    _decode_int,
    _decode_float,
    _decode_string,
    _decode_bool,
    _decode_bytes,
    _decode_list,
    _decode_dict,
    _decode_ndarray,
    _decode_dataframe,
]


def encode(py_value: PY_TYPES_) -> pb.Value:
    """Encode a Python value to a Value proto."""
    for ser_type, encoder in zip(PY_TYPES, _ENCODERS):
        if type(py_value) == ser_type:
            pb_value = encoder(py_value)
            return pb_value

    raise Exception(f"Type '{type(py_value)}' not in accepted types '{PY_TYPES}'")


def decode(pb_value: pb.Value) -> PY_TYPES_:
    """Decode a Value proto to a Python value."""
    return _DECODERS[pb_value.type - 1](pb_value)
