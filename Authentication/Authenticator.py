import jwt
from flask import current_app


class Authenticator:
    @staticmethod
    def get_role(token):
        try:
            secret = current_app.config['TOKEN_KEY']
            decoded_token = jwt.decode(token, secret)
        except:
            return None
        else:
            return decoded_token.role

    @staticmethod
    def authenticate_admin(token):
        role = Authenticator.get_role(token)
        if role != "admin":
            raise Exception("Only a logged in admin can take this action here!")

    @staticmethod
    def authenticate_employee(token):
        role = Authenticator.get_role(token)
        if role != "employee":
            raise Exception("Only a logged in employee can take this action here!")
