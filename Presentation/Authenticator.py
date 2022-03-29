import jwt
from flask import current_app


class Authenticator:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Authenticator, cls).__new__(cls)
        return cls.instance

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
            return "Only a logged in admin can take this action here!"

    @staticmethod
    def authenticate_employee(token):
        role = Authenticator.get_role(token)
        if role != "employee":
            return "Only a logged in admin or employee can take this action here!"

