from DataAccess.Room import RoomDataAccess


class Room:
    def __init__(self, name, capacity, office, white_board, video_projector):
        self.name = name
        self.capacity = capacity
        self.office = office
        self.white_board = white_board
        self.video_projector = video_projector
        self.insert_to_database()

    def insert_to_database(self):
        data_access = RoomDataAccess()
        data_access.insert_room(self.name, self.capacity, self.office, self.white_board, self.video_projector)

    @staticmethod
    def get_room_by_name(name):
        data_access = RoomDataAccess()
        room_data = data_access.get_room_data(name)
        return Room(room_data[0]['name'], room_data[0]['capacity'], room_data[0]['office'], room_data[0]['white_board'],
                    room_data[0]['video_projector'])

    def update_capacity(self, capacity):
        data_access = RoomDataAccess()
        self.capacity = capacity
        data_access.update_capacity(self.name, capacity)

    def update_office(self, office):
        data_access = RoomDataAccess()
        self.office = office
        data_access.update_office(self.name, office)

    def update_white_board(self, white_board):
        data_access = RoomDataAccess()
        self.white_board = white_board
        data_access.update_white_board(self.name, white_board)

    def update_video_projector(self, video_projector):
        data_access = RoomDataAccess()
        self.video_projector = video_projector
        data_access.update_video_projector(self.name, video_projector)

    def delete_room(self):
        data_access = RoomDataAccess()
        data_access.delete_room(self.name)

    def get_room_data(self):
        data_access = RoomDataAccess()
        return data_access.get_room_data(self.name)

    @staticmethod
    def get_all_rooms():
        data_access = RoomDataAccess()
        return data_access.get_all_rooms()
