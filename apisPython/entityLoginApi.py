from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid
import logging

app = Flask(__name__)

# Simulación de bases de datos
hidden_users_db = {"admin": "securepassword"}  # Base de datos oculta para el login inicial
tokens_db = []  # Lista para almacenar tokens generados
users_db = {
    "12345678-9": {"password": "userpass", "token": None},  # Ejemplo de usuario con RUT
    "98765432-1": {"password": "anotherpass", "token": None},
}  # Base de datos de usuarios con RUT, contraseña y token

# Método para generar un token único
def generate_token():
   token = str(uuid.uuid4())
   return token


# Login "oculto" para obtener un token

logging.basicConfig(level=logging.DEBUG)

@app.route('/hidden_login', methods=['POST'])
def hidden_login():
    data = request.get_json()
    logging.debug(f"Hidden Login Request: {data}")
    username = data.get("username")
    password = data.get("password")
    if username in hidden_users_db and hidden_users_db[username] == password:
        token = generate_token()
        tokens_db.append(token)
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    logging.debug(f"User Login Request: {data}")
    rut = data.get("rut")
    password = data.get("password")
    token = data.get("token")
    if token not in tokens_db:
        return jsonify({"error": "Invalid token"}), 401
    user = users_db.get(rut)
    if user and user["password"] == password:
        user["token"] = token
        return jsonify({"message": "Login successful", "rut": rut}), 200
    else:
        return jsonify({"error": "Invalid RUT or password"}), 401

# Método protegido que requiere autenticación
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get("Authorization")
    if not token or token not in tokens_db:
        return jsonify({"error": "Unauthorized access"}), 401

    rut = request.args.get("rut")
    user = users_db.get(rut)
    if user and user["token"] == token:
        return jsonify({"message": f"Welcome, user with RUT {rut}!"}), 200
    else:
        return jsonify({"error": "Invalid RUT or token mismatch"}), 403

if __name__ == '__main__':
    app.run(host="192.168.120.8", port=5000, debug=True)
