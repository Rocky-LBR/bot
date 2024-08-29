from functools import wraps

from flask import request

from common import LOGIN_SECRET


def token_required():
    def check_token(f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            jwt_token = request.headers.get("token", None)
            if not jwt_token:
                return {'error':'User unauthorized'},401

            try:
                user_info = jwt.decode(jwt_token,LOGIN_SECRET,algorithms='HS256')
                if not user_info or not user_info.get('username',None):
                    return {'error':'User unauthorized'},401
            except Exception as e:
                return {'error':'User unauthorized'},401
            result = f(*args,**kwargs)
            return result
        return check_token()
