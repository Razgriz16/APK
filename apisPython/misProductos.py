from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database
products_db = {}
product_counter = 1

# Product categories
default_products = ["cuenta capitalización"]
possible_products = ["cuenta ahorro", "crédito en cuotas", "línea de crédito en cuotas", "línea de crédito rotativa", "depósito a plazo"]

@app.route("/products", methods=["POST"])
def create_product():
    global product_counter
    data = request.json
    user_products = list(set(data["prod"] + default_products))  # Ensure "cuenta capitalización" is always included

    product_data = {
        "cod": product_counter,
        "userCode": data["userCode"],
        "prod": user_products
    }

    products_db[product_counter] = product_data
    product_counter += 1
    return jsonify(product_data), 201

@app.route("/products/<int:user_code>", methods=["GET"])
def get_user_products(user_code):
    user_products = [p for p in products_db.values() if p["userCode"] == user_code]
    return jsonify(user_products if user_products else {"error": "No products found for this user"})

if __name__ == "__main__":
    app.run(host="192.168.120.8", port=5001)
