# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: esdbclient/protos/Grpc/status.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

from esdbclient.protos.Grpc import (
    code_pb2 as esdbclient_dot_protos_dot_Grpc_dot_code__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#esdbclient/protos/Grpc/status.proto\x12\ngoogle.rpc\x1a\x19google/protobuf/any.proto\x1a!esdbclient/protos/Grpc/code.proto"`\n\x06Status\x12\x1e\n\x04\x63ode\x18\x01'
    b" \x01(\x0e\x32\x10.google.rpc.Code\x12\x0f\n\x07message\x18\x02"
    b" \x01(\t\x12%\n\x07\x64\x65tails\x18\x03"
    b" \x01(\x0b\x32\x14.google.protobuf.AnyBa\n\x0e\x63om.google.rpcB\x0bStatusProtoP\x01Z7google.golang.org/genproto/googleapis/rpc/status;status\xf8\x01\x01\xa2\x02\x03RPCb\x06proto3"
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "esdbclient.protos.Grpc.status_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.rpcB\013StatusProtoP\001Z7google.golang.org/genproto/googleapis/rpc/status;status\370\001\001\242\002\003RPC"
    _STATUS._serialized_start = 113
    _STATUS._serialized_end = 209
# @@protoc_insertion_point(module_scope)
