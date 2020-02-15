import jwt, datetime
from config import BaseConfig

# TODO: Add other required payloads.
def get_auth_token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return jwt.encode({'exp': expiration_date}, BaseConfig.SECRET_KEY, algorithm='HS256')