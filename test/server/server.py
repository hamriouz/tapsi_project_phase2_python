import grpc
from concurrent import futures

from pymongo import MongoClient

from test.server.proto import room_pb2, room_pb2_grpc

connection_string = "mongodb://127.0.0.1:27017/rooms"
client = MongoClient(connection_string)
db = client.get_database("rooms")
collection = db.get_collection("roomDetail")


class RoomServicer(room_pb2_grpc.RoomServicer):
    def getDetails(self, request, context):
        print("sth")
        # print(request)
        # print(request.capacity)
        room_data = {"name": "name",
                     "capacity": 1236,
                     "office": "office",
                     "whiteboard": True,
                     "projector": False}

        collection.insert_one(room_data)
        print(request.capacity)
        filter = {"capacity": request.capacity}
        cursor = collection.find(filter, {'_id': False})
        wanted_rooms = []
        for each_document in cursor:
            wanted_rooms.append(each_document)
        print(wanted_rooms)

        # return ([{"name": "name",
        #           "capacity": 1236,
        #           "office": "office",
        #           "whiteboard": True,
        #           "projector": False}])
        return room_pb2.RoomResponse(rooms=wanted_rooms)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    room_pb2_grpc.add_RoomServicer_to_server(RoomServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()
