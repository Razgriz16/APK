
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulated database
users_db = {}
user_counter = 1

@app.route("/users", methods=["POST"])
def create_user():
    global user_counter
    data = request.json
    user_data = {
        "cod": user_counter,
        "rut": data["rut"],
        "password": data["password"],
        "token": str(uuid.uuid4())  # Generate a unique token
    }
    users_db[user_counter] = user_data
    user_counter += 1
    return jsonify(user_data), 201

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(users_db.get(user_id, {"error": "User not found"}))

if __name__ == "__main__":
    app.run(host="192.168.120.8", port=5000)

