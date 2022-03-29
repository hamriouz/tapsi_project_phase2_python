from DataAccess.Room import RoomDataAccess
from Domain.Room import Room


class RoomDomain:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RoomDomain, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def create_room(room_name, capacity, office, white_board, video_projector):
        Room(room_name, capacity, office, white_board, video_projector)

    @staticmethod
    def update_capacity(room_name, room_capacity):
        room = Room.get_room_by_name(room_name)
        room.update_capacity(room_capacity)

    @staticmethod
    def update_office(room_name, office):
        room = Room.get_room_by_name(room_name)
        room.update_office(office)

    @staticmethod
    def update_white_board(room_name, white_board):
        room = Room.get_room_by_name(room_name)
        room.update_white_board(white_board)

    @staticmethod
    def update_video_projector(room_name, video_projector):
        room = Room.get_room_by_name(room_name)
        room.update_video_projector(video_projector)

    @staticmethod
    def delete_room(room_name):
        room = Room.get_room_by_name(room_name)
        room.delete_room()

    @staticmethod
    def get_room_data(room_name):
        room = Room.get_room_by_name(room_name)
        return room.get_room_data()

    @staticmethod
    def get_all_rooms():
        return Room.get_all_rooms()
