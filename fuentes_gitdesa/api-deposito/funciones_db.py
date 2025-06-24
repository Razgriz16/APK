import cx_Oracle
from cx_Oracle import SessionPool
import yaml

# Función para crear un session pool
def create_session_pool(db_config):
    pool = SessionPool(
        user=db_config['user'],
        password=db_config['password'],
        dsn=db_config['tns_alias'],  # Usar el alias de TNS
        min=db_config.get('min_pool_size', 2),
        max=db_config.get('max_pool_size', 10),
        increment=db_config.get('increment', 1)
    )
    return pool

#################################################
# Cargar la configuración desde el archivo YAML #
#################################################
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)


##############################################
#######           Crear el pool           ####
##############################################
db_config = config['database']
pool = create_session_pool(db_config)


##############################################
# Función para obtener una conexión del pool #
##############################################
def get_connection():
    return pool.acquire()


#########################################
##########   IN PAR, OUT CURSOR  ########
#########################################
def pkg_exe_par_cursor(procedure_name, package_name, params):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                # Crear la llamada al procedimiento
                sql_call = f"BEGIN {package_name}.{procedure_name}({', '.join([':' + str(i+1) for i in range(len(params) + 1)] )}); END;"

                # Crear una variable para el cursor de salida
                out_cursor = cursor.var(cx_Oracle.CURSOR)

                # Preparar los parámetros, agregando el cursor de salida al final
                procedure_params = list(params) + [out_cursor]

                # Ejecutar el procedimiento
                cursor.execute(sql_call, procedure_params)

                # Obtener el cursor de salida
                ref_cursor = out_cursor.getvalue()

                # Si hay resultados, convertirlos a JSON
                if ref_cursor:
                    # Obtener los nombres de las columnas
                    columns = [col[0].lower() for col in ref_cursor.description]
                    # Obtener las filas y convertirlas en una lista de diccionarios
                    results = [dict(zip(columns, row)) for row in ref_cursor]
                    return {"data":results}, 200  # Devuelve los resultados y el código de estado 200
                else:
                    return {"data":[]}, 200  # Devuelve una lista vacía si no hay resultados

    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return {"error": str(e)}, 500  # Devuelve un mensaje de error y el código de estado 500



#####################################################
######   IN PAR, OUT P_ERROR, OUT P_MSG, OUT CURSOR  ########
#####################################################
def pkg_exe_par_error_msg_cursor(procedure_name, package_name, params):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                # Crear variables para los parámetros de salida
                p_error = cursor.var(cx_Oracle.NUMBER)
                p_msg_error = cursor.var(cx_Oracle.STRING)
                out_cursor = cursor.var(cx_Oracle.CURSOR)

                # Crear la llamada al procedimiento
                # Número de parámetros de entrada
                num_input_params = len(params)
                # Crear placeholders para los parámetros de entrada
                input_placeholders = ", ".join([f":{i+1}" for i in range(num_input_params)])
                
                print(input_placeholders)
                # Agregar placeholders para los parámetros de salida
                sql_call = f"""
                    BEGIN
                        {package_name}.{procedure_name}(
                            {input_placeholders},
                            :{num_input_params + 1},
                            :{num_input_params + 2},
                            :{num_input_params + 3}
                        );
                    END;
                """

                # Combinar parámetros de entrada y salida
                procedure_params = params + [p_error, p_msg_error, out_cursor]

                # Ejecutar el procedimiento
                cursor.execute(sql_call, procedure_params)

                # Obtener los valores de los parámetros de salida
                error_code = p_error.getvalue()
                error_message = p_msg_error.getvalue()
                ref_cursor = out_cursor.getvalue()

                # Verificar si hubo un error
                if error_code != 0:
                    return {"error": error_message}, 400  # Devuelve el mensaje de error y código 400

                # Si hay resultados en el cursor, convertirlos a JSON
                if ref_cursor:
                    # Obtener los nombres de las columnas
                    columns = [col[0].lower() for col in ref_cursor.description]
                    # Obtener las filas y convertirlas en una lista de diccionarios
                    results = [dict(zip(columns, row)) for row in ref_cursor]
                    return {"data": results, "error_code": error_code, "error_message": error_message}, 200
                else:
                    return {"data": [], "error_code": error_code, "error_message": error_message}, 200

    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return {"error": str(e)}, 500  # Devuelve un mensaje de error y el código de estado 500

#####################################################
######   OUT P_ERROR, OUT P_MSG, OUT CURSOR  ########
#####################################################
def pkg_exe_error_msg_cursor(procedure_name, package_name, params):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                # Crear variables para los parámetros de salida
                p_error = cursor.var(cx_Oracle.NUMBER)
                p_msg_error = cursor.var(cx_Oracle.STRING)
                out_cursor = cursor.var(cx_Oracle.CURSOR)

                # Crear la llamada al procedimiento
                sql_call = f"""
                    BEGIN
                        {package_name}.{procedure_name}(
                            :1,
                            :2,
                            :3
                        );
                    END;
                """

                # Ejecutar el procedimiento
                cursor.execute(sql_call, [p_error, p_msg_error, out_cursor])

                # Obtener los valores de los parámetros de salida
                error_code = p_error.getvalue()
                error_message = p_msg_error.getvalue()
                ref_cursor = out_cursor.getvalue()

                # Verificar si hubo un error
                if error_code != 0:
                    return {"error": error_message}, 400  # Devuelve el mensaje de error y código 400

                # Si hay resultados en el cursor, convertirlos a JSON
                if ref_cursor:
                    # Obtener los nombres de las columnas
                    columns = [col[0].lower() for col in ref_cursor.description]
                    # Obtener las filas y convertirlas en una lista de diccionarios
                    results = [dict(zip(columns, row)) for row in ref_cursor]
                    return {"data": results, "error_code": error_code, "error_message": error_message}, 200
                else:
                    return {"data": [], "error_code": error_code, "error_message": error_message}, 200

    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return {"error": str(e)}, 500  # Devuelve un mensaje de error y el código de estado 500



#################################################################
######   IN PAR, OUT P_ERROR, OUT P_MSG, OUT COLLECTION  ########
#################################################################
def pkg_exe_par_error_msg_collection(procedure_name, package_name, params, collection_type_name):
#En esta caso params tiene que ser un diccionario no una lista
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                # Crear variables para los parámetros de salida
                p_error = cursor.var(cx_Oracle.NUMBER)
                p_msg_error = cursor.var(cx_Oracle.STRING)

                # Obtener el tipo de colección desde la base de datos
                collection_type = connection.gettype(collection_type_name)
                p_collection = cursor.var(collection_type)

                # Construir la llamada al procedimiento dinámicamente
                param_placeholders = ", ".join(f":{key}" for key in params.keys())
                sql_call = f"""
                    BEGIN
                        {package_name}.{procedure_name}(
                            {param_placeholders},
                            :P_ERROR,
                            :P_MSG_ERROR,
                            :P_COLLECTION
                        );
                    END;
                """

                # Agregar los parámetros de salida al diccionario de entrada
                params["P_ERROR"] = p_error
                params["P_MSG_ERROR"] = p_msg_error
                params["P_COLLECTION"] = p_collection

                # Ejecutar el procedimiento
                cursor.execute(sql_call, params)

                # Obtener los valores de los parámetros de salida
                error_code = p_error.getvalue()
                error_message = p_msg_error.getvalue()
                collection = p_collection.getvalue()

                # Verificar si hubo un error
                if error_code != 0:
                    return {"error": error_message}, 400

                # Procesar la colección
                results = []
                if collection:
                    for item in collection.aslist():
                        # Convertir cada elemento de la colección en un diccionario
                        results.append({
                            attr.name.lower(): getattr(item, attr.name)
                            for attr in item.type.attributes
                        })

                return {"data": results, "error_code": error_code, "error_message": error_message}, 200

    except cx_Oracle.DatabaseError as e:
        print(f"Database error in {package_name}.{procedure_name}: {e}")
        return {"error": f"Database error in {package_name}.{procedure_name}: {str(e)}"}, 500


##################################
######   IN PAR, OUT NUMBER  #####
##################################
def pkg_exe_par_number(procedure_name, package_name, params):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                # Crear variable para el parámetro de salida (cadena de texto)
                out_number = cursor.var(cx_Oracle.NUMBER)

                # Crear placeholders para los parámetros de entrada
                input_placeholders = ", ".join(f":{key}" for key in params.keys())

                # Construir la llamada SQL al procedimiento
                sql_call = f"""
                    BEGIN
                        {package_name}.{procedure_name}(
                            {input_placeholders},
                            :P_OUTPUT
                        );
                    END;
                """

                # Agregar el parámetro de salida al diccionario de parámetros
                params["P_OUTPUT"] = out_number

                # Ejecutar el procedimiento
                cursor.execute(sql_call, params)

                # Obtener el valor del parámetro de salida
                out_int = out_number.getvalue()

                return {"data": out_int},200

    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return {"error": str(e), "error_code": 500}
