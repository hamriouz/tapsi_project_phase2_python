from Domain.Controller import RoomDomain
from Exception.Exceptions import IncompleteInformationException


class RequestHandler:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RequestHandler, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def insert_room(room_record):
        print(room_record)
        room_name = room_record["name"]
        capacity = room_record["capacity"]
        office = room_record["office"]
        white_board = room_record["white_board"]
        video_projector = room_record["video_projector"]
        if room_name and capacity and office and white_board and video_projector is not None:
            room_domain = RoomDomain()
            room_domain.create_room(room_name, capacity, office, white_board, video_projector)
        else:
            raise IncompleteInformationException

    @staticmethod
    def update_room(room_record):
        room_name = room_record["name"]
        capacity = room_record["capacity"]
        office = room_record["office"]
        white_board = room_record["white_board"]
        video_projector = room_record["video_projector"]
        room_domain = RoomDomain()

        if room_name is not None:
            if capacity is not None:
                room_domain.update_capacity(room_name, capacity)
            if office is not None:
                room_domain.update_office(room_name, office)
            if white_board is not None:
                room_domain.update_white_board(room_name, white_board)
            if video_projector is not None:
                room_domain.update_video_projector(room_name, video_projector)
            new_room_data = room_domain.get_room_data(room_name)
            return new_room_data
        else:
            raise IncompleteInformationException

    @staticmethod
    def delete_room(room_record):
        room_name = room_record["name"]
        if room_name is not None:
            room_domain = RoomDomain()
            room_domain.delete_room(room_name)
        else:
            raise IncompleteInformationException

    @staticmethod
    def get_all_rooms():
        room_domain = RoomDomain()
        all_rooms = room_domain.get_all_rooms()
        return all_rooms
