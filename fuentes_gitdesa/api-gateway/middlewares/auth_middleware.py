import jwt 
from functools import wraps
from flask import request, jsonify, current_app
from config import config


public_url = ['/v1/cliente/auth/login']


def auth_jwt(f):
    @wraps(f)
    def decorador(*args,**kwargs):
        current_app.logger.info(request.path)
        if request.path in public_url:
            current_app.logger.info("ruta publica")
            return f(*args,**kwargs)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith('Bearer'):
            return jsonify({"error":"Header de autorizacion incorrect o faltante"}),401

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                config['gateway']['jwt_secret_key'],
                algorithms=[config['gateway']['jwt_algorithm']]
            )
            request.user = payload
            current_app.logger.info("Decoded JWT payload:", payload)
            if payload.get('type') != 'access':
                return jsonify({"error":"Token incorrecto"}),401
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"Token expirado"}),401
        except jwt.InvalidTokenError:
            return jsonify({"error":"Token incorrecto"}),401
        return f(*args,**kwargs)
    return decorador

