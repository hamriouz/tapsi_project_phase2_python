class AddRoomException(Exception):
    def __init__(self):
        message = "Only a logged in admin can add rooms!"
        super().__init__(message)


class NotLoggedInException(Exception):
    def __init__(self):
        message = "You are not logged in!"
        super().__init__(message)


class UpdateRoomException(Exception):
    def __init__(self):
        message = "Only a logged in admin can update rooms!"
        super().__init__(message)


class DeleteRoomException(Exception):
    def __init__(self):
        message = "Only a logged in admin can delete rooms!"
        super().__init__(message)


class IncompleteInformationException(Exception):
    def __init__(self):
        message = 'please fill in all the information'
        super().__init__(message)

