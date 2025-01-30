from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database
balances_db = {}
balance_counter = 1

@app.route("/balances", methods=["POST"])
def create_balance():
    global balance_counter
    data = request.json

    # Ensure each product has its own balance
    balance_data = {
        "cod": balance_counter,
        "userCode": data["userCode"],
        "saldo": data["saldo"]  # Example: {"cuenta capitalización": 1000, "cuenta ahorro": 500}
    }

    balances_db[balance_counter] = balance_data
    balance_counter += 1
    return jsonify(balance_data), 201

@app.route("/balances/<int:user_code>", methods=["GET"])
def get_user_balance(user_code):
    user_balances = [b for b in balances_db.values() if b["userCode"] == user_code]
    return jsonify(user_balances if user_balances else {"error": "No balance found for this user"})

if __name__ == "__main__":
    app.run(debug="192.168.120.8", port=5002)
