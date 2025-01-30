from flask import Flask, request, jsonify


app = Flask(__name__)


test = {"user": "juan", "password": "123456"}, {"user":"jesus" , "password": "123456"}

@app.route('/user', methods=['GET'])
def get_all_users():
    return (test)


if __name__ == "__main__":
    app.run(host="192.168.120.8", port=5000)

