# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from test.server.proto import room_pb2 as gRPC_dot_proto_dot_room__pb2


class RoomStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getRoomIdentifier = channel.unary_unary(
                '/room.Room/getRoomIdentifier',
                request_serializer=gRPC_dot_proto_dot_room__pb2.RoomIdentifierRequest.SerializeToString,
                response_deserializer=gRPC_dot_proto_dot_room__pb2.RoomIdentifierResponse.FromString,
                )
        self.getRoomCapacity = channel.unary_unary(
                '/room.Room/getRoomCapacity',
                request_serializer=gRPC_dot_proto_dot_room__pb2.RoomCapacityRequest.SerializeToString,
                response_deserializer=gRPC_dot_proto_dot_room__pb2.RoomCapacityResponse.FromString,
                )


class RoomServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getRoomIdentifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getRoomCapacity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoomServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getRoomIdentifier': grpc.unary_unary_rpc_method_handler(
                    servicer.getRoomIdentifier,
                    request_deserializer=gRPC_dot_proto_dot_room__pb2.RoomIdentifierRequest.FromString,
                    response_serializer=gRPC_dot_proto_dot_room__pb2.RoomIdentifierResponse.SerializeToString,
            ),
            'getRoomCapacity': grpc.unary_unary_rpc_method_handler(
                    servicer.getRoomCapacity,
                    request_deserializer=gRPC_dot_proto_dot_room__pb2.RoomCapacityRequest.FromString,
                    response_serializer=gRPC_dot_proto_dot_room__pb2.RoomCapacityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'room.Room', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Room(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getRoomIdentifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/room.Room/getRoomIdentifier',
            gRPC_dot_proto_dot_room__pb2.RoomIdentifierRequest.SerializeToString,
            gRPC_dot_proto_dot_room__pb2.RoomIdentifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getRoomCapacity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/room.Room/getRoomCapacity',
            gRPC_dot_proto_dot_room__pb2.RoomCapacityRequest.SerializeToString,
            gRPC_dot_proto_dot_room__pb2.RoomCapacityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
