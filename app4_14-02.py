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
    token = request.headers.get('Authorization')
    data = request.get_json()
    rut = data.get("rut")
    password = data.get("password")

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


# Login for users with RUT, password, and token
@app.route('/cuenta_cap/<rut>', methods=['GET'])
def cuenta_cap(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT A.CUENTA, A.SALDOCONTABLE, TO_CHAR(A.FECHAAPERTURA,'DD-MM-YYYY') AS FECHAAPERTURA, B.NOMBRE
                           FROM CSOCIAL.CUENTA A, CSOCIAL.PRODUCTO B 
                           WHERE A.CODIGOPRODUCTO = B.CODIGOPRODUCTO AND A.RUTTITULAR = :rut"""  # Parameterized query!

            result = execute_query(saldo_query, {"rut": rut}) # Make sure execute_query uses parameters

            if result:
                account_data = {  # Correct dictionary creation
                    "NROCUENTA": result[0][0],  # Access elements correctly
                    "SALDOCONTABLE": format(result[0][1], ",.0f").replace(",", "."),
                    "FECHAAPERTURA": result[0][2],
                    "TIPOCUENTA": result[0][3]
                }
                return jsonify(account_data), 200 # Correct variable name
            else:
                return jsonify({"error": "Cuenta no encontrada"}), 404

        except Exception as e: # Catch potential errors
            print(f"An error occurred: {e}") # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500 # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401 # Use appropriate status code (401 Unauthorized)
"""
    # Autorización: Verifica que el usuario puede acceder a la información del RUT
    if current_user_rut != rut:
        return jsonify({"error": "Unauthorized"}), 403 # Forbidden
"""

# Movements for users with token and rut
@app.route('/movimientos/<rut>', methods=['GET'])
def movimientos(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """  SELECT * FROM (SELECT CS.CUENTA,
         TO_CHAR(CS.FECHAPAGO,'DD-MM-YYYY'),
         CS.MONTO,
         TR.NOMBRE,
         TR.NOMBREABREVIADO,
         TR.ESCARGO,
         SUC.NOMBRE AS SUCURSAL
    FROM CSOCIAL.MOVIMIENTO CS,
         CSOCIAL.TRANSACCION TR,
         CSOCIAL.CUENTA CTA,
         SGT.SUCURSAL SUC
   WHERE     CS.CODIGOTRANSACCION = TR.CODIGOTRANSACCION
         AND CTA.CUENTA = CS.CUENTA
         AND CTA.CODIGOSUCURSAL = SUC.CODIGOSUCURSAL
         AND CTA.RUTTITULAR = :rut
   ORDER BY CS.FECHAPAGO DESC)
   WHERE ROWNUM <=25

 """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                account_data = []
                for row in result:
                    account_data.append({
                        "CUENTA": row[0],
                        "FECHAPAGO": row[1],
                        "MONTO": format(row[2],",.0f").replace(",", "."),
                        "NOMBRETRANSACCION": row[3],
                        "NOMBREABRTRANSACCION": row[4],
                        "ESCARGO": row[5]
                    })
                return jsonify({"movimientos": account_data}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Movimientos no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)

# Savings account
@app.route('/cuenta_ahorro/<rut>', methods=['GET'])
def cuenta_ahorro(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT P.NOMBRE, C.SALDODISPONIBLE, C.SALDOCONTABLE, S.NOMBRE, TO_CHAR( C.FECHAAPERTURA, 'DD-MM-YYYY'), TO_NUMBER (
                        TRIM (C.CODIGOSISTEMA)
                     || TRIM (TO_CHAR (C.CODIGOSUCURSAL, '000'))
                     || TRIM (TO_CHAR (C.NUMEROCUENTA, '0000000'))
                     || TRIM (C.DIGITOCUENTA))
                     AS NROCUENTA FROM AHORRO.CUENTAAHORRO C, AHORRO.PRODUCTO P, SGT.SUCURSAL S WHERE C.CODIGOPRODUCTO = P.CODIGOPRODUCTO AND S.CODIGOSUCURSAL = C.CODIGOSUCURSAL AND C.RUTTITULAR1 = :rut """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                account_data = []
                for row in result:
                    account_data.append({
                        "TIPOCUENTA": row[0],
                        "SALDODISPONIBLE": format(row[1],",.0f").replace(",", "."),
                        "SALDOCONTABLE": format(row[2],",.0f").replace(",", "."),
                        "SUCURSAL": row[3],
                        "FECHAAPERTURA": row[4],
                        "NROCUENTA": row[5]
                    })
                return jsonify({"ahorro": account_data}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Ahorros no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)


# Movements for users with token and rut
@app.route('/movimientos_ahorro/<rut>', methods=['GET'])
def movimientos_ahorro(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT * FROM (
    SELECT
        MOV.MONTO,
        TO_CHAR(MOV.FECHAEFECTIVA, 'DD-MM-YYYY') AS FECHA,
        TRA.NOMBRE,
        TRA.NOMBREABREVIADO,
        TRA.CARGOABONO,
        SUC.NOMBRE AS SUCURSAL,
        TO_NUMBER (
            TRIM (CTA.CODIGOSISTEMA)
            || TRIM (TO_CHAR (CTA.CODIGOSUCURSAL, '000'))
            || TRIM (TO_CHAR (CTA.NUMEROCUENTA, '0000000'))
            || TRIM (CTA.DIGITOCUENTA)
        ) AS NROCUENTA,
        ROW_NUMBER() OVER (PARTITION BY CTA.NUMEROCUENTA ORDER BY MOV.FECHAEFECTIVA DESC) AS RN
    FROM AHORRO.MOVIMIENTOS MOV
    JOIN AHORRO.TRANSACCION TRA ON MOV.CODIGOTRANSACCION = TRA.CODIGOTRANSACCION
    JOIN AHORRO.CUENTAAHORRO CTA ON MOV.NUMEROCUENTA = CTA.NUMEROCUENTA
    JOIN SGT.SUCURSAL SUC ON MOV.CODIGOSUCURSAL = SUC.CODIGOSUCURSAL AND CTA.SUCURSALCONTABLE = SUC.CODIGOSUCURSAL
    WHERE CTA.RUTTITULAR1 = :RUT
) WHERE RN <= 20
"""

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                account_data = []
                for row in result:
                    account_data.append({
                        "MONTO": format(row[0],",.0f").replace(",", "."),
                        "FECHAMOV": row[1],
                        "NOMBRETRANSAC": row[2],
                        "NOMBRETRANSACABRV": row[3],
                        "CARGOABONO": row[4],
                        "NOMBRESUCURSAL": row[5],
                        "NROCUENTA": row[6]
                    })
                return jsonify({"movimientos_ahorro": account_data}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Movimientos no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)

# Savings account
@app.route('/credito_cuotas/<rut>', methods=['GET'])
def credito_cuotas(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT A.CREDITO AS NROCUENTA,
       P.DESCRIPCION AS TIPOCUENTA,
       A.CUOTAS AS NUMEROCUOTAS,
       A.MONTOLIQUIDO AS MONTOCREDITO,
       A.VALORCUOTA AS VALORCUOTA,
       TO_CHAR (CUO.FECHAVENCIMIENTO, 'DD-MM-YYYY') PROXVENCIMIENTO,
       A.CEDULA AS RUT
  FROM CREDITO.CREDITO A,
       CREDITO.PRODUCTO P,
       (SELECT CREDITO, MIN (FECHAVENCIMIENTO) AS FECHAVENCIMIENTO
            FROM CREDITO.CUOTA
           WHERE ESTADO >= 0
        GROUP BY CREDITO) CUO
 WHERE  A.CREDITO = CUO.CREDITO
 AND    A.PRODUCTO = P.CODIGO
 AND    A.CEDULA = :rut

 """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                credito_cuotas = []
                for row in result:
                    credito_cuotas.append({
                        "NROCUENTA": row[0],
                        "TIPOCUENTA": row[1],
                        "NUMEROCUOTAS": row[2],
                        "MONTOCREDITO": format(row[3],",.0f").replace(",", "."),
                        "VALORCUOTA": format(row[4],",.0f").replace(",", "."),
                        "PROXVENCIMIENTO": row[5]
                    })
                return jsonify({"credito_cuotas": credito_cuotas}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Ahorros no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)


# Movements for users with token and rut
@app.route('/movimientos_creditos/<rut>', methods=['GET'])
def movimientos_credidos(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "rut is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT * FROM (SELECT T.NOMBRE,
        M.MONTOMOVIMIENTO AS MONTO,
        TO_CHAR(M.FECHAHORA,'DD-MM-YYYY') AS FECHA,
        SUC.NOMBRE AS SUCURSAL,
        M.CREDITO AS CREDITO
FROM    CREDITO.MOVIMIENTODIARIO  M,
        CREDITO.TIPOMOVIMIENTO T,
        SGT.SUCURSAL SUC,
        CREDITO.CREDITO C
WHERE M.TIPOMOVIMIENTO = T.CODIGO
AND M.SUCURSAL = SUC.CODIGOSUCURSAL
AND M.CREDITO = C.CREDITO
AND C.CEDULA =:rut
ORDER BY M.FECHAHORA DESC)
WHERE ROWNUM <= 25
 """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                account_data = []
                for row in result:
                    account_data.append({
                        "NOMBRE": row[0],
                        "MONTO":format(row[1],",.0f").replace(",", "."),
                        "FECHA": row[2],
                        "SUCURSAL": row[3],
                        "NROCUENTA": row[4]
                    })
                return jsonify({"movimientos_creditos": account_data}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Movimientos no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)

# LCC
@app.route('/lcc/<rut>', methods=['GET'])
def lcc(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "RUT is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """
            SELECT LCC.CODIGO, LCC.CUPOOTORGADO AS CUPO_AUTORIZADO, LCC.CUPOUTILIZADO, LCC.MONTORETENIDO AS CUPODISPONIBLE
FROM LINEACC.LINEADECREDITO LCC WHERE RUTCLIENTE =: rut
 """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                lcc = []
                for row in result:
                    lcc.append({
                        "NROCUENTA": row[0],
                        "CUPOAUTORIZADO": format(row[1],",.0f").replace(",", "."),
                        "CUPOUTILIZADO": format(row[2],",.0f").replace(",", "."),
                        "CUPODISPONIBLE": format(row[3],",.0f").replace(",", ".")
                    })
                return jsonify({"lcc": lcc}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Ahorros no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)

# Movements for users with token and rut
@app.route('/movimientos_lcc/<rut>', methods=['GET'])
def movimientos_lcc(rut):
    token = request.headers.get('Authorization')
    #data = request.get_json()
    #rut = data.get("rut")

    if not rut:
        return jsonify({"error": "rut is required"}), 400

    if validacion(token):  # Important: Ensure robust token validation
        try:
            saldo_query = """SELECT *
  FROM (  SELECT M.LINEADECREDITO AS OPERACION,
                 T.DESCRIPCION AS TIPOMOVIMIENTO,
                 TO_CHAR (M.FECHAREALIZACION, 'dd-mm-yyyy') AS FECHA,
                 S.NOMBRE AS SUCURSAL,
                 M.MONTOMOVIMIENTO AS MONTO
            FROM LINEACC.MOVIMIENTODIARIO M,
                 LINEACC.LINEADECREDITO C,
                 LINEACC.TIPOMOVIMIENTO T,
                 SGT.SUCURSAL S
           WHERE     M.TIPOMOVIMIENTO = T.CODIGO
                 AND M.SUCURSAL = S.CODIGOSUCURSAL
                 AND M.LINEADECREDITO = C.CODIGO
                 AND C.RUTCLIENTE = :rut
        ORDER BY M.FECHAREALIZACION DESC)
WHERE ROWNUM <= 20
 """

            result = execute_query(saldo_query, {"rut": rut})  # Make sure execute_query uses parameters

            if result:
                account_data = []
                for row in result:
                    account_data.append({
                        "NROCUENTA": row[0],
                        "TIPOMOVIMIENTO": row[1],
                        "FECHA": row[2],
                        "SUCURSAL": row[3],
                        "MONTO": format(row[4],",.0f").replace(",", ".")
                    })
                return jsonify({"movimientos_lcc": account_data}), 200  # Correct variable name and structure for JSON response
            else:
                return jsonify({"error": "Movimientos no encontrados"}), 404

        except Exception as e:  # Catch potential errors
            print(f"An error occurred: {e}")  # Log the error for debugging
            return jsonify({"error": "An internal server error occurred"}), 500  # Don't expose internal error details to the user

    else:
        return jsonify({"error": "Invalid token"}), 401  # Use appropriate status code (401 Unauthorized)

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
            SELECT 12,'LCC' FROM LINEACC.LINEADECREDITO WHERE RUTCLIENTE = :RUT AND ESTADO = 1
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

