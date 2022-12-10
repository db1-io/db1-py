#!/bin/bash

SRC="../serializer-interface/v_01/"
SRC_FILE="serializer.proto"
DST="./db1/_protos/serializer"

protoc ${SRC_FILE} --proto_path=${SRC} --python_out=${DST} --mypy_out=${DST}
