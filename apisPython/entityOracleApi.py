from flask import Flask, request, jsonify
import uuid
import cx_Oracle

app = Flask(__name__)

# Oracle database connection details
DB_USER = "mantencion"
DB_PASSWORD = "m4ntenc10n_prod"
DB_DSN = "192.168.80.120/prodt.oriencoop.cl"  # Replace with your DSN or connection string

# Establish a connection pool (recommended for production)
connection_pool = cx_Oracle.SessionPool(
    user=DB_USER,
    password=DB_PASSWORD,
    dsn=DB_DSN,
    min=2,
    max=10,
    increment=1
)

# Method to generate a unique token
def generate_token():
    return str(uuid.uuid4())

# Helper function to execute queries
def execute_query(query, params=None, commit=False):
    try:
        with connection_pool.acquire() as connection:
            with connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                if commit:
                    connection.commit()
                return cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return None

# Hidden login to obtain a token
@app.route('/hidden_login', methods=['POST'])
def hidden_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Query to check credentials in the database
    query = "SELECT FROM SGT.API_ENTIDAD WHERE USERNAME = :username AND PASSWORD = :password"
    result = execute_query(query, {"USERNAME": username, "PASSWORD": password})
    if result and result[0][0] > 0:  # If credentials are valid
        token = generate_token()

        # Store the token in the tokens table
        insert_query = "UPDATE SGT.API_ENTIDAD SET TOKEN = :token WHERE COD = 1"
        execute_query(insert_query, {"TOKEN": token}, commit=True)

        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Login for users with RUT, password, and token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    rut = data.get("rut")
    password = data.get("password")
    token = data.get("token")

    # Check if the token exists in the tokens table
    token_query = "SELECT COUNT(*) FROM tokens WHERE token = :token"
    token_result = execute_query(token_query, {"token": token})
    if not token_result or token_result[0][0] == 0:
        return jsonify({"error": "Invalid token"}), 401

    # Check if the RUT and password match in the users table
    user_query = "SELECT COUNT(*) FROM users WHERE rut = :rut AND password = :password"
    user_result = execute_query(user_query, {"rut": rut, "password": password})
    if user_result and user_result[0][0] > 0:
        # Associate the token with the user in the users table
        update_query = "UPDATE users SET token = :token WHERE rut = :rut"
        execute_query(update_query, {"token": token, "rut": rut}, commit=True)

        return jsonify({"message": "Login successful", "rut": rut}), 200
    else:
        return jsonify({"error": "Invalid RUT or password"}), 401

# Protected endpoint requiring authentication
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get("Authorization")
    rut = request.args.get("rut")

    # Check if the token exists in the tokens table
    token_query = "SELECT COUNT(*) FROM tokens WHERE token = :token"
    token_result = execute_query(token_query, {"token": token})
    if not token_result or token_result[0][0] == 0:
        return jsonify({"error": "Unauthorized access"}), 401

    # Check if the RUT and token match in the users table
    user_query = "SELECT COUNT(*) FROM users WHERE rut = :rut AND token = :token"
    user_result = execute_query(user_query, {"rut": rut, "token": token})
    if user_result and user_result[0][0] > 0:
        return jsonify({"message": f"Welcome, user with RUT {rut}!"}), 200
    else:
        return jsonify({"error": "Invalid RUT or token mismatch"}), 403

if __name__ == '__main__':
    app.run(host="192.168.120.8", port = 5001, debug=True)
