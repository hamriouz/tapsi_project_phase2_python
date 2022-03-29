from flask import request, current_app

from Presentation.Authenticator import Authenticator


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
