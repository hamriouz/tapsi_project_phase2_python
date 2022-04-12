# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC/proto/room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gRPC/proto/room.proto\x12\x04room\"9\n\x15RoomIdentifierRequest\x12\x0e\n\x06office\x18\x01 \x01(\t\x12\x10\n\x08roomName\x18\x02 \x01(\t\"0\n\x16RoomIdentifierResponse\x12\x16\n\x0eroomIdentifier\x18\x01 \x01(\t\"-\n\x13RoomCapacityRequest\x12\x16\n\x0eroomIdentifier\x18\x01 \x01(\t\"(\n\x14RoomCapacityResponse\x12\x10\n\x08\x63\x61pacity\x18\x01 \x01(\x05\x32\xa4\x01\n\x04Room\x12P\n\x11getRoomIdentifier\x12\x1b.room.RoomIdentifierRequest\x1a\x1c.room.RoomIdentifierResponse\"\x00\x12J\n\x0fgetRoomCapacity\x12\x19.room.RoomCapacityRequest\x1a\x1a.room.RoomCapacityResponse\"\x00\x62\x06proto3')



_ROOMIDENTIFIERREQUEST = DESCRIPTOR.message_types_by_name['RoomIdentifierRequest']
_ROOMIDENTIFIERRESPONSE = DESCRIPTOR.message_types_by_name['RoomIdentifierResponse']
_ROOMCAPACITYREQUEST = DESCRIPTOR.message_types_by_name['RoomCapacityRequest']
_ROOMCAPACITYRESPONSE = DESCRIPTOR.message_types_by_name['RoomCapacityResponse']
RoomIdentifierRequest = _reflection.GeneratedProtocolMessageType('RoomIdentifierRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROOMIDENTIFIERREQUEST,
  '__module__' : 'gRPC.proto.room_pb2'
  # @@protoc_insertion_point(class_scope:room.RoomIdentifierRequest)
  })
_sym_db.RegisterMessage(RoomIdentifierRequest)

RoomIdentifierResponse = _reflection.GeneratedProtocolMessageType('RoomIdentifierResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROOMIDENTIFIERRESPONSE,
  '__module__' : 'gRPC.proto.room_pb2'
  # @@protoc_insertion_point(class_scope:room.RoomIdentifierResponse)
  })
_sym_db.RegisterMessage(RoomIdentifierResponse)

RoomCapacityRequest = _reflection.GeneratedProtocolMessageType('RoomCapacityRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROOMCAPACITYREQUEST,
  '__module__' : 'gRPC.proto.room_pb2'
  # @@protoc_insertion_point(class_scope:room.RoomCapacityRequest)
  })
_sym_db.RegisterMessage(RoomCapacityRequest)

RoomCapacityResponse = _reflection.GeneratedProtocolMessageType('RoomCapacityResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROOMCAPACITYRESPONSE,
  '__module__' : 'gRPC.proto.room_pb2'
  # @@protoc_insertion_point(class_scope:room.RoomCapacityResponse)
  })
_sym_db.RegisterMessage(RoomCapacityResponse)

_ROOM = DESCRIPTOR.services_by_name['Room']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROOMIDENTIFIERREQUEST._serialized_start=31
  _ROOMIDENTIFIERREQUEST._serialized_end=88
  _ROOMIDENTIFIERRESPONSE._serialized_start=90
  _ROOMIDENTIFIERRESPONSE._serialized_end=138
  _ROOMCAPACITYREQUEST._serialized_start=140
  _ROOMCAPACITYREQUEST._serialized_end=185
  _ROOMCAPACITYRESPONSE._serialized_start=187
  _ROOMCAPACITYRESPONSE._serialized_end=227
  _ROOM._serialized_start=230
  _ROOM._serialized_end=394
# @@protoc_insertion_point(module_scope)
