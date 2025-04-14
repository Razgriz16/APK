import jwt
from datetime import datetime, timedelta
from typing import Dict, Optional
import os
from functools import wraps
from flask import request, jsonify


class JWTManager:
    def __init__(self):
        self.secret_key = os.environ.get('JWT_SECRET_KEY', 'SECRET_DESARROLLO')
        self.access_token_exp_min = int(os.environ.get('ACCESS_EXP_MIN', 5))
        self.refresh_token_exp_dia = int(os.environ.get('REFRESH_EXP_DIAS', 7))

        # En producción, esto será una base de datos
        self.refresh_token_db: Dict[str, str] = {}

    def generar_access_token(self, id_usuario: int) -> str:
        """
        Genera el access token
        """
        payload = {
            'id_usuario': id_usuario,
            'exp': datetime.utcnow() + timedelta(minutes=self.access_token_exp_min),
            'iat': datetime.utcnow(),
            'type': 'access'
        }

        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def generar_refresh_token(self, id_usuario: int) -> str:
        """
        Genera el refresh token
        """
        payload = {
            'id_usuario': id_usuario,
            'exp': datetime.utcnow() + timedelta(days=self.refresh_token_exp_dia),
            'iat': datetime.utcnow(),
            'type': 'refresh'
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        self.refresh_token_db[str(id_usuario)] = token  # Guardar el token en memoria por ahora
        return token

    def verificar_token(self, token: str, type: str = None) -> Optional[dict]:
        """
        Verifica token y retorna su payload si es válido
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            if type and payload.get('type') != type:
                return None
            return payload
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None

    def token_requerido(self, f):
        """
        Decorator para proteger rutas con JWT
        """
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({"error": "Token de autorización requerido"}), 401

            if not auth_header.startswith('Bearer'):
                return jsonify({'error': 'Formato de token no válido'}), 401

            token = auth_header[7:]
            payload = self.verificar_token(token, 'access')
            if not payload:
                return jsonify({"error": "Token inválido o expirado"}), 401

            # Agregar el payload al request
            request.jwt_payload = payload
            return f(*args, **kwargs)

        return decorated

    def invalidar_refresh_token(self, id_usuario: str) -> bool:
        """
        Invalida un refresh token
        """
        if str(id_usuario) in self.refresh_token_db:
            del self.refresh_token_db[str(id_usuario)]
            return True
        return False


# Instancia singleton
jwt_manager = JWTManager()
