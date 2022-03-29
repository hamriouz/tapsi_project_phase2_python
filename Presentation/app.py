import json

from flask import Flask, request, jsonify, make_response, current_app
from Authentication.Authenticator import Authenticator

from Exception.Exceptions import AddRoomException, IncompleteInformationException, NotLoggedInException, \
    UpdateRoomException, DeleteRoomException
from Handler.RoomRequestHandler import RequestHandler

app = Flask(__name__)


def check_employee_or_admin(function):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is not None:
            authenticator = Authenticator()
            result = authenticator.authenticate_admin(token)
            if result is None:
                return current_app.ensure_sync(function)(token, *args, **kwargs)
            else:
                result = None
                result = authenticator.authenticate_employee(token)
                if result is None:
                    return current_app.ensure_sync(function)(*args, **kwargs)
                else:
                    return {"message": result}, 401
        return {"message": "Only a logged admin or employee can take this action"}, 401

    wrapper.__name__ = function.__name__
    return wrapper


def check_admin(function):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is not None:
            authenticator = Authenticator()
            result = authenticator.authenticate_admin(token)
            if result is None:
                return current_app.ensure_sync(function)(*args, **kwargs)
            else:
                return {"message": "Only a logged admin can take this action"}, 401
        else:
            return {"message": "Only a logged admin can take this action"}, 401

    wrapper.__name__ = function.__name__
    return wrapper


@app.route('/RoomManagement/InsertRoom', methods=['POST'])
# @check_admin
def insert_room():
    try:
        request_handler = RequestHandler()
        record = json.loads(request.data)
        request_handler.insert_room(record)
        message = {"message": "The room was successfully created!"}
        return make_response(jsonify(message), 200)
    except AddRoomException:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 400)
    except IncompleteInformationException:
        message = {"message": "please fill in all the information"}
        return make_response(jsonify(message), 401)


@app.route('/RoomManagement/GetRooms', methods=['GET'])
# @check_employee_or_admin
def get_rooms():
    try:
        request_handler = RequestHandler()
        all_rooms = request_handler.get_all_rooms()
        return {"all rooms": all_rooms}, 200
    except NotLoggedInException:
        message = {"message": "You are not logged in!"}
        return make_response(jsonify(message), 400)
    except IncompleteInformationException:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 401)


@app.route('/RoomManagement/UpdateRoom', methods=['POST'])
@check_admin
def update_rooms():
    try:
        request_handler = RequestHandler
        record = json.loads(request.data)
        request_handler.update_room(record)
        new_room_data = request_handler.update_room(record)
        return make_response(jsonify(new_room_data), 200)
    except UpdateRoomException:
        message = {"message": "Only a logged in admin can update rooms!"}
        return make_response(jsonify(message), 400)
    except IncompleteInformationException:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 401)


@app.route('/RoomManagement/DeleteRoom', methods=['POST'])
# @check_admin
def delete_rooms():
    try:
        request_handler = RequestHandler()
        record = json.loads(request.data)
        request_handler.delete_room(record)
        message = {"message": "The selected room was successfully deleted!"}
        return make_response(jsonify(message), 200)
    except DeleteRoomException:
        message = {"message": "Only a logged in admin can delete rooms!"}
        return make_response(jsonify(message), 400)
    except IncompleteInformationException:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 401)
