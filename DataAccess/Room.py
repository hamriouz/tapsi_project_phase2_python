import json

from bson import json_util
from pymongo import MongoClient


def get_database_collection():
    connection_string = "mongodb://127.0.0.1:27017/rooms"
    client = MongoClient(connection_string)
    db = client.get_database("rooms")
    data_base_collection = db.get_collection("roomDetail")
    return data_base_collection


class RoomDataAccess:
    __instance = None

    @staticmethod
    def get_instance():
        if RoomDataAccess.__instance is None:
            RoomDataAccess()
        return RoomDataAccess.__instance

    @staticmethod
    def insert_room(name, capacity, office, white_board, video_projector):
        data_base_collection = get_database_collection()
        room_data = {"name": name,
                     "capacity": capacity,
                     "office": office,
                     "white_board": white_board,
                     "video_projector": video_projector}
        data_base_collection.insert_one(room_data)

    @staticmethod
    def get_all_rooms():
        data_base_collection = get_database_collection()
        rooms_in_db = data_base_collection.find()
        return json.loads(json_util.dumps(rooms_in_db))

    @staticmethod
    def update_capacity(name, capacity):
        data_base_collection = get_database_collection()
        data_base_collection.update_one({"name": name},
                                        {
                                            "$set": {"capacity": capacity}
                                        })

    @staticmethod
    def update_office(name, office):
        data_base_collection = get_database_collection()
        data_base_collection.update_one({"name": name},
                                        {
                                            "$set": {"office": office}
                                        })

    @staticmethod
    def update_white_board(name, white_board):
        data_base_collection = get_database_collection()
        data_base_collection.update_one({"name": name},
                                        {
                                            "$set": {"white_board": white_board}
                                        })

    @staticmethod
    def update_video_projector(name, video_projector):
        data_base_collection = get_database_collection()
        if video_projector != "":
            data_base_collection.update_one({"name": name},
                                            {
                                                "$set": {"video_projector": video_projector}
                                            })

    @staticmethod
    def get_room_data(name):
        data_base_collection = get_database_collection()
        wanted_room_filter = {"name": name}
        return data_base_collection.find(wanted_room_filter)

    @staticmethod
    def delete_room(name):
        data_base_collection = get_database_collection()
        data_base_collection.delete_one({"name": name})
