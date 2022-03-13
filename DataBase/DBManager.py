import json

from bson import json_util


class DBManager:

    @staticmethod
    def add_room(name, capacity, office, white_board, video_projector, collection):
        room_data = {"name": name,
                     "capacity": capacity,
                     "office": office,
                     "white_board": white_board,
                     "video_projector": video_projector}

        collection.insert_one(room_data)

    @staticmethod
    def get_all_rooms(collection):
        rooms_in_db = collection.find()
        return json.loads(json_util.dumps(rooms_in_db))

    @staticmethod
    def modify_room(room_name, capacity, office, white_board, video_projector, collection):
        if capacity != "":
            collection.update_one({"name": room_name},
                                  {
                                      "$set": {"capacity": capacity}
                                  })
        if office != "":
            collection.update_one({"name": room_name},
                                  {
                                      "$set": {"office": office}
                                  })
        if white_board != "":
            collection.update_one({"name": room_name},
                                  {
                                      "$set": {"white_board": white_board}
                                  })
        if video_projector != "":
            collection.update_one({"name": room_name},
                                  {
                                      "$set": {"video_projector": video_projector}
                                  })

        wanted_room_filter = {"name": room_name}
        return collection.find(wanted_room_filter)

    @staticmethod
    def delete_room(room_name, collection):
        collection.delete_one({"name": room_name})








    # ===============================================

    # from pymongo import MongoClient

    ## set up database:
    # connection_string = "mongodb://127.0.0.1:27017/inventory"
    # client = MongoClient(connection_string)
    # db = client.get_database("inventory")
    #
    # collection = db.get_collection("items")

    ##delete
    # result = collection.delete_one({"item": "sth"})
    # print(result)

    ##insert
    # document = {"item": "sth", "qty": 100, "tags": ["cotton"]}
    #
    # response = collection.insert_one(document)
    # last_inserted_id = response.inserted_id
    # print("last : {}".format(last_inserted_id))
    #
    # # more than one item:
    # documents = []
    # documents.append({"one": 1})
    # documents.append({"two": 2})
    #
    # response2 = collection.insert_many(documents)

    # cursor = collection.find()
    # print("==============")
    # for each_document in cursor:
    #     print(each_document)

    # print(client.list_database_names())

    # db_instance = client.get_database("local")
    # print(db_instance.list_collection_names())

    # filter = {"qty": 100, "item": "sth"}
    # cursor = collection.find(filter)
    # for each_document in cursor:
    #     print(each_document)
# DBManager().add_room("naaaa", "caaaa", "offf", ["asss", "sdgjhsagdjyhgas"], collection)
# DBManager().add_room("name", "caaaa", "offf", ["asss", "sdgjhsagdjyhgas"], collection)
# DBManager().add_room("naaaaaame", "caaaa", "offf", ["asss","sdgjhsagdjyhgas"], collection)
# # print(DBManager().get_all_rooms(collection))
# # DBManager().delete_room("naaaaaame",collection)
# DBManager().modify_room("name", "dwdqwd", "", "", collection)
#
# print(DBManager().get_all_rooms(collection))

# def modify_room(room_name, capacity, office, features, collection):

# room_data = {"name": "name",
#              "capacity": "capacity",
#              "office": "office",
#              "features": "features"}
#
# collection.insert_one(room_data)
#
# all_rooms = []
# rooms_in_db = collection.find()
# for room in rooms_in_db:
#     print(room)
#
# # collection.replace_one({"name": "name"}, {"capacity": "3333"})
# collection.update_one({"name": "name"},
#                       {
#                           "$set": {"capacity": "123124"}
#                       })
#
#
#
#
# # collection.update_one({"name": "name"}, {"capacity": 2})
#
#
# all_rooms = []
# rooms_in_db = collection.find()
# for room in rooms_in_db:
#     print(room)
