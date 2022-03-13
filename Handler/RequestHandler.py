from DataBase.DBManager import DBManager


class RequestHandler:
    @staticmethod
    def add_room(record, collection):
        room_name = record["name"]
        capacity = record["capacity"]
        office = record["office"]
        white_board = record["white_board"]
        video_projector = record["video_projector"]
        DBManager().add_room(room_name, capacity, office, white_board, video_projector, collection)

    @staticmethod
    def modify_room(record, collection):
        room_name = record["name"]
        capacity = record["capacity"]
        office = record["office"]
        white_board = record["white_board"]
        video_projector = record["video_projector"]
        new_room_data = DBManager().modify_room(room_name, capacity, office, white_board, video_projector, collection)
        return new_room_data

    @staticmethod
    def delete_room(record, collection):
        room_name = record["name"]
        DBManager().delete_room(room_name, collection)

