import json
from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from Authentication.Authenticator import Authenticator
from DataBase.DBManager import DBManager
from Handler.RequestHandler import RequestHandler

connection_string = "mongodb://127.0.0.1:27017/rooms"
client = MongoClient(connection_string)
db = client.get_database("rooms")
collection = db.get_collection("roomDetail")

app = Flask(__name__)


@app.route('/RoomManagement/AddRoom/Admin', methods=['POST'])
def add_room():
    token = request.headers.get('Authorization')
    try:
        Authenticator().authenticate_admin(token)
    except:
        message = {"message": "Only a logged in admin can add rooms!"}
        return make_response(jsonify(message), 400)
    else:
        record = json.loads(request.data)
        RequestHandler.add_room(record, collection)
        message = {"message": "The room was successfully created!"}
        return make_response(jsonify(message), 200)


@app.route('/RoomManagement/GetRooms/Admin', methods=['GET'])
def get_rooms_admin():
    token = request.headers.get('Authorization')
    try:
        Authenticator().authenticate_admin(token)
    except:
        message = {"message": "Only a logged in admin can see the created rooms!"}
        return make_response(jsonify(message), 400)
    else:
        all_rooms = DBManager().get_all_rooms(collection)
        return {"all rooms": all_rooms}, 200


@app.route('/RoomManagement/ModifyRoom/Admin', methods=['POST'])
def modify_rooms():
    token = request.headers.get('Authorization')
    try:
        Authenticator().authenticate_admin(token)
    except:
        message = {"message": "Only a logged in admin can modify rooms!"}
        return make_response(jsonify(message), 400)
    else:
        record = json.loads(request.data)
        new_room_data = RequestHandler.modify_room(record, collection)
        return make_response(jsonify(new_room_data), 200)


@app.route('/RoomManagement/DeleteRoom/Admin', methods=['POST'])
def delete_rooms():
    token = request.headers.get('Authorization')
    try:
        Authenticator().authenticate_admin(token)
    except:
        message = {"message": "Only a logged in admin can delete rooms!"}
        return make_response(jsonify(message), 400)
    else:
        record = json.loads(request.data)
        RequestHandler.delete_room(record, collection)
        message = {"message": "The selected room was successfully deleted!"}
        return make_response(jsonify(message), 200)


@app.route('/RoomManagement/GetRooms/Employee', methods=['GET'])
def get_rooms_employee():
    token = request.headers.get('Authorization')
    try:
        Authenticator().authenticate_employee(token)
    except:
        message = {"message": "Only a logged in employee can see the created rooms!"}
        return make_response(jsonify(message), 400)
    else:
        all_rooms = DBManager().get_all_rooms(collection)
        return {"all rooms": all_rooms}, 200

# if __name__ == '__main__':
#     app.run(debug=True)

# You can delete objects by using the del keyword:
#
# Example
# Delete the p1 object:
#
# del p1


# set cookie
# @app.route('/setcookie', methods=['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['nm']
#
#     resp = make_response(render_template('readcookie.html'))
#     resp.set_cookie('userID', user)
#
#     return resp

# get cookie
# @app.route('/getcookie')
# def getcookie():
#    name = request.cookies.get('userID')
#    return '<h1>welcome ' + name + '</h1>'


# {
#     "name": "Tehran",
# "capacity": 12,
# "features":"whiteboad",
# "office":"asdsad"
# }
