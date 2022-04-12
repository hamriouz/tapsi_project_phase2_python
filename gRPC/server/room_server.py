from concurrent import futures

import grpc
from bson.objectid import ObjectId
from pymongo import MongoClient

import room_pb2
import room_pb2_grpc

connection_string = "mongodb://127.0.0.1:27017/rooms"
client = MongoClient(connection_string)
db = client.get_database("rooms")
collection = db.get_collection("roomDetail")


class RoomServicer(room_pb2_grpc.RoomServicer):
    def getRoomIdentifier(self, request, context):
        room_identifier_filter = {"name": request.name, "office": request.office}
        room_id = collection.find_one(room_identifier_filter)["_id"]
        return room_pb2.RoomIdentifierResponse(room_id=room_id)

    def getRoomCapacity(self, request, context):
        room_id = request.room_identifier
        obj_instance = ObjectId(room_id)
        capacity = collection.find_one({"_id": obj_instance})["capacity"]
        return room_pb2.RoomCapacityResponse(capacity=capacity)

    def getAllRoomsInOffice(self, request, context):
        office = request.office
        office_filter = {"office": office}
        all_rooms = collection.find(office_filter)
        return room_pb2.RoomsInOffice(AllRoomsInOffice=all_rooms)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    room_pb2_grpc.add_RoomServicer_to_server(RoomServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()
