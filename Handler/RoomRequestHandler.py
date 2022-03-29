from Domain.Room import Room
from Util.Exceptions import IncompleteInformationException


class RequestHandler:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RequestHandler, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def insert_room(room_record):
        room_name = room_record["name"]
        capacity = room_record["capacity"]
        office = room_record["office"]
        white_board = room_record["white_board"]
        video_projector = room_record["video_projector"]
        if room_name and capacity and office and white_board and video_projector is not None:
            Room(room_name, capacity, office, white_board, video_projector)
        else:
            raise IncompleteInformationException

    @staticmethod
    def update_room(room_record):
        room_name = room_record["name"]
        capacity = room_record["capacity"]
        office = room_record["office"]
        white_board = room_record["white_board"]
        video_projector = room_record["video_projector"]
        room = Room.get_room_by_name(room_name)

        if room_name is not None:
            if capacity is not None:
                room.update_capacity(capacity)
            if office is not None:
                room.update_office(office)
            if white_board is not None:
                room.update_white_board(white_board)
            if video_projector is not None:
                room.update_video_projector(video_projector)
            new_room_data = room.get_room_data()
            return new_room_data
        else:
            raise IncompleteInformationException

    @staticmethod
    def delete_room(room_record):
        room_name = room_record["name"]
        if room_name is not None:
            room = Room.get_room_by_name(room_name)
            room.delete_room()
        else:
            raise IncompleteInformationException

    @staticmethod
    def get_all_rooms():
        all_rooms = Room.get_all_rooms()
        return all_rooms
