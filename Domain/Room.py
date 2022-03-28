from DataAccess.Room import RoomDataAccess


class RoomDomain:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RoomDomain, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def insert_room(room_name, capacity, office, white_board, video_projector):
        data_access = RoomDataAccess()
        data_access.insert_room(room_name, capacity, office, white_board, video_projector)

    @staticmethod
    def update_capacity(room_name, room_capacity):
        data_access = RoomDataAccess()
        data_access.update_capacity(room_name, room_capacity)

    @staticmethod
    def update_office(room_name, office):
        data_access = RoomDataAccess()
        data_access.update_office(room_name, office)

    @staticmethod
    def update_white_board(room_name, white_board):
        data_access = RoomDataAccess()
        data_access.update_white_board(room_name, white_board)

    @staticmethod
    def update_video_projector(room_name, video_projector):
        data_access = RoomDataAccess()
        data_access.update_video_projector(room_name, video_projector)

    @staticmethod
    def delete_room(room_name):
        data_access = RoomDataAccess()
        data_access.delete_room(room_name)

    @staticmethod
    def get_room_data(room_name):
        data_access = RoomDataAccess()
        return data_access.get_room_data(room_name)

    @staticmethod
    def get_all_rooms():
        data_access = RoomDataAccess()
        return data_access.get_all_rooms()

