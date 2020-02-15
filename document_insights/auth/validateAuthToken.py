from flask import Flask, jsonify, request, Response
from config import BaseConfig
from functools import wraps
import jwt
from ..constants.stringContants import stringContants

#This decorator uses uses authorization header to  read the token and validate.
def authorize(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            try:
                # Try to decode the token
                jwt.decode(auth_token, BaseConfig.SECRET_KEY)
                return f(*args, **kwargs)
            except:
                return jsonify({stringContants.ERROR : stringContants.INVALID_TOKEN}), 401
        else:
            return jsonify({stringContants.ERROR : stringContants.INVALID_TOKEN}), 401
    return wrapper