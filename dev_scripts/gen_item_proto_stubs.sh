#!/bin/bash

SRC="../db1-app/proto-defs/"
SRC_FILE="item-cr-0v1.proto"
DST="./db1/_protos/item"

protoc ${SRC_FILE} --proto_path=${SRC} --python_out=${DST} --mypy_out=${DST}
