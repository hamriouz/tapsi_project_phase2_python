import json

from flask import Flask, request, jsonify, make_response
from Authentication.Authenticator import Authenticator
from functools import wraps

from Handler.RoomRequestHandler import RequestHandler

app = Flask(__name__)


def check_admin():
    def _check_admin(f):
        @wraps(f)
        def __check_admin(*args, **kwargs):
            token = request.headers.get('Authorization')
            authenticator = Authenticator()
            authenticator.authenticate_admin(token)
            result = f(*args, **kwargs)
            return result

        return __check_admin

    return _check_admin


def check_employee_or_admin():
    def _check_employee_or_admin(f):
        @wraps(f)
        def __check_employee_or_admin(*args, **kwargs):
            token = request.headers.get('Authorization')
            authenticator = Authenticator()
            authenticator.authenticate_admin(token)
            result = f(*args, **kwargs)
            return result

        return __check_employee_or_admin

    return _check_employee_or_admin


# todo!
@app.before_request
def before_request_func():
    token = request.headers.get('Authorization')
    authenticator = Authenticator()
    authenticator.authenticate_admin(token)


@app.route('/RoomManagement/InsertRoom', methods=['POST'])
def insert_room():
    try:
        request_handler = RequestHandler()
        record = json.loads(request.data)
        request_handler.insert_room(record)
        message = {"message": "The room was successfully created!"}
        return make_response(jsonify(message), 200)
    except:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 400)


@app.route('/RoomManagement/GetRooms', methods=['GET'])
def get_rooms():
    try:
        request_handler = RequestHandler()
        all_rooms = request_handler.get_all_rooms()
        return {"all rooms": all_rooms}, 200
    except:
        message = {"message": "You are not logged in!"}
        return make_response(jsonify(message), 400)


@app.route('/RoomManagement/UpdateRoom', methods=['POST'])
def update_rooms():
    try:
        request_handler = RequestHandler
        record = json.loads(request.data)
        request_handler.update_room(record)
        new_room_data = request_handler.update_room(record)
        return make_response(jsonify(new_room_data), 200)
    except:
        message = {"message": "Only a logged in admin can modify rooms!"}
        return make_response(jsonify(message), 400)


@app.route('/RoomManagement/DeleteRoom', methods=['POST'])
def delete_rooms():
    try:
        request_handler = RequestHandler()
        record = json.loads(request.data)
        request_handler.delete_room(record)
        message = {"message": "The selected room was successfully deleted!"}
        return make_response(jsonify(message), 200)
    except:
        message = {"message": "Only a logged in admin can delete rooms!"}
        return make_response(jsonify(message), 400)
