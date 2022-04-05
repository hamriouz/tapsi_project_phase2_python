# from pymongo import MongoClient
# from bson.objectid import ObjectId
#
#
#
# class Test:
#     @staticmethod
#     def start_db():
#         connection_string = "mongodb://127.0.0.1:27017/rooms"
#         client = MongoClient(connection_string)
#         db = client.get_database("rooms")
#         return db.get_collection("roomDetail")
#
#     @staticmethod
#     def test_get_id():
#         collection = Test.start_db()
#         # room_data = {"name": "name",
#         #              "capacity": 1236,
#         #              "office": "office",
#         #              "whiteboard": True,
#         #              "projector": False}
#         #
#         # collection.insert_one(room_data)
#         # room_filter = {"name": "name", "office": "office"}
#
#         # print(cursor)
#
#
# #622f4f28a8fe255ff5eaaed6
#
# Test.test_get_id()