from flask import Flask, request, jsonify
import uuid
import cx_Oracle
import time

app = Flask(__name__)

# Oracle database connection details
DB_USER = "mantencion"
DB_PASSWORD = "m4ntenc10n_prod"
DB_DSN = "192.168.80.120:1521/prodt.oriencoop.cl"  # Replace with your DSN or connection string

# Establish a connection pool (recommended for production)
connection_pool = cx_Oracle.SessionPool(
    user=DB_USER,
    password=DB_PASSWORD,
    dsn=DB_DSN,
    min=2,
    max=5,
    increment=1
)

# Method to generate a unique token
def generate_token():
    return str(uuid.uuid4())

# Helper function to execute queries
def execute_query(query, params=None, commit=False, fetch_results=True):
    try:
        with connection_pool.acquire() as connection:
            with connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                if commit:
                    connection.commit()
                if fetch_results:
                    return cursor.fetchall()
                else:
                    return None
    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return None

def validacion(token):
    # Check if the token exists in the tokens table
    token_query = "SELECT TOKEN FROM SGT.API_ENTIDAD WHERE token = :token"
    token_result = execute_query(token_query, {"token": token})
    if token_result:
        return True
    else:
        return False

@app.before_request
def log_request_info():
    app.logger.info("Request Method: %s", request.method)
    app.logger.info("Request URL: %s", request.url)
    app.logger.info("Request Headers: %s", request.headers)
    app.logger.info("Request Body: %s", request.get_data())


@app.route('/public_data', methods=['GET'])
def public_data():
    """
    Endpoint para obtener datos públicos sin autenticación.
    """
    try:
        # Consulta a la base de datos para obtener los datos públicos.
        # Aquí deberías especificar la lógica para obtener los datos que 
        # quieres exponer públicamente.  No incluyas información sensible.
        # Ejemplo: Obtener una lista de productos, categorías, etc.

        # Placeholder de la consulta (ADAPTAR A TU BASE DE DATOS):
        query = "SELECT USERNAME, PASSWORD FROM SGT.API_ENTIDAD"
        results = execute_query(query)

        # Formatear los resultados para la respuesta JSON.
        # Asegúrate de serializar correctamente los datos para JSON.
        data_to_return = []
        for row in results:
            data_to_return.append({
                "USERNAME": row[0],
                "PASSWORD": row[1]
                 # ... otros campos
            })


        return jsonify(data_to_return), 200

    except Exception as e:
        print(f"Error en /public_data: {e}") # Log del error (importante!)
        return jsonify({"error": "Error al obtener los datos"}), 500  # Error genérico para el cliente

# Hidden login to obtain a token
@app.route('/hidden_login', methods=['POST'])
def hidden_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    # Query to check credentials in the database
    query = "SELECT COD, USERNAME FROM SGT.API_ENTIDAD WHERE USERNAME = :username AND PASSWORD = :password"
    result = execute_query(query, {"username": username, "password": password})
    if result:  # If credentials are valid
        user_cod = result[0][0] #
        token = generate_token()
        # Store the token in the tokens table
        insert_query = "UPDATE SGT.API_ENTIDAD SET TOKEN = :token WHERE COD = :user_cod" #cambiar por codigo respectivo de la entidad
        execute_query(insert_query, {"TOKEN": token, "user_cod": user_cod}, commit=True, fetch_results= False)
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

    if validacion(token) == True:
        # Check if the RUT and password match in the users table
        user_query = "SELECT RUTCLIENTE FROM CLIENTE.CLAVEINTERNET  WHERE RUTCLIENTE = :rut AND CLAVE = :password"
        user_result = execute_query(user_query, {"rut": rut, "password": password})
        if user_result:
            return jsonify({"message": "Login successful", "rut": rut}), 200
        else:
            return jsonify({"error": "Invalid RUT or password"}), 401
    else:
        return "token malo\n"

@app.route('/productos/<rut>', methods=['GET'])
def productos(rut):
    # Verificar token
    token = request.headers.get('Authorization')
    if not token or not validacion(token):
        return jsonify({"error": "Token invalido o no proporcionado"}), 401

    # Definir todos los productos posibles
    productos = {
        'CREDITO': 0,
        'AHORRO': 0,
        'DEPOSTO': 0,
        'LCC': 0,
        'LCR': 0,
        'CSOCIAL': 0
    }

    try:
        # Consulta SQL
        query = """
            SELECT 6,'CREDITO' AS PRODUCTO FROM CREDITO.CREDITO WHERE CEDULA = :RUT AND ESTADO = 2
            UNION
            SELECT 3,'AHORRO' FROM AHORRO.CUENTAAHORRO WHERE RUTTITULAR1 = :RUT AND ESTADOCUENTA = 2
            UNION
            SELECT 2,'DEPOSTO' FROM DEPOSITO.OPERACION WHERE RUTCLIENTE = :RUT AND ESTADO = 20
            UNION
            SELECT 12,'LCC' FROM LINEACC.LINEADECREDITO WHERE RUTCLIENTE = :RUT AND ESTADO = 2
            UNION
            SELECT 10,'LCR' FROM LINEACRD.LINEACREDITO WHERE CLIENTE = :RUT AND ESTADO = 2
            UNION
            SELECT 8,'CSOCIAL' FROM CSOCIAL.CUENTA WHERE RUTTITULAR = :RUT AND ESTADO = 2
        """
        resultados = execute_query(query, {"RUT":rut})

        # Actualizar productos existentes
        for resultado in resultados:
            producto = resultado[1]
            if producto in productos:
                productos[producto] = 1

        return jsonify(productos)

    except cx_Oracle.Error as error:
        return jsonify({"error": f"Error de base de datos: {error}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)

