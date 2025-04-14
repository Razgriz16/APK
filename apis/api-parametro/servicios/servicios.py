import funciones_db


def validar_respuesta(response):
    """
    Valida la estructura de la respuesta y maneja errores comunes.
    
    Args:
        response (dict): Respuesta del servicio.
    
    Returns:
        tuple: Mensaje de error y código de estado, si corresponde.
    """
    if not isinstance(response, dict) or "data" not in response:
        return {"error": "Respuesta del servidor inválida"}, 500

    if len(response["data"]) == 0:
        return {"error": "No se encontraron resultados"}, 404

    return None, None


def get_sucursales_activas():
    """
    Servicio obtener las sucursales activas
    Args:
	None
    Return: Devuelve las sucursales activas
    """
    try:
        response, status_code = recuperar_sucursales_activas()
        error_response, error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code
        return {
            "data": response["data"],
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500


def get_sucursal_por_codigo(codigo):
    """
    Servicio obtener sucursal por codigo 
    Args:
	codigo:int
    Return: Si el codigo es valido devuelve la sucursal 
    """
    if not codigo:
        return {"error":"Faltan parametros"},400
    try:
        response, status_code = obtener_sucursal(codigo)
        error_response, error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code

   
        return {
            "data": response["data"],
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500

def get_comunas(comuna=-1,ciudad=-1):
    """
    Servicio obtener las comunas
    Args:
	comuna:int
	ciudad:int
    Return: retorna informacion de la comuna/s
    """
    if not isinstance(comuna,int) or not isinstance(ciudad,int):
        return {"error":"Codigo ciudad y codigo comuna tiene que ser enteros"} , 400

    try:
        response, status_code = obtener_comunas(comuna,ciudad)
        error_response, error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code

        return {
            "data": response["data"],
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500

def get_ciudades(ciudad=-1):
    """
    Servicio obtener las ciudades
    Args:
	ciudad:int
    Return: retorna informacion de la ciudad/es
    """

    try:
        response, status_code = obtener_ciudades(ciudad)
        error_response, error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code

        return {
            "data": response["data"],
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500

def get_parametros_sgt(ciudad=-1):
    """
    Servicio obtener las ciudades
    Args:
	ciudad:int
    Return: retorna informacion de la ciudad/es
    """

    try:
        response, status_code = obtener_parametros()
        error_response, error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code

        return {
            "data": response["data"],
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500



###################################################
######    Recuperar sucucursales activas  #########
###################################################
def recuperar_sucursales_activas():
    package_name = "SGT.PCK_SGT"  
    procedure_name = "SGTRECSUCURSALES"

    params = []

    response, status_code = funciones_db.pkg_exe_no_params_cursor(procedure_name, package_name)

    # Devolver la respuesta en formato JSON
    return response, status_code



#############################################
######    Recuperar una sucucursal  #########
#############################################
def obtener_sucursal(codigo):

    package_name = "SGT.PCK_SGT"
    procedure_name = "obtener_sucursal"

    params = [codigo]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return response, status_code

###########################################
#### Recuperar cumuna(s)    ###############
###########################################
def obtener_comunas(comuna,ciudad):
    package_name = "SGT.PCK_SGT"
    procedure_name = "SGTRECCOMUNAS"

    # Parámetros para el procedimiento (en este caso, solo el RUT)
    params = [comuna,ciudad]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return response, status_code

def obtener_ciudades(ciudad):
    package_name = "SGT.PCK_SGT"  # Reemplaza con el nombre de tu package
    procedure_name = "SGTRECCIUDADES"  # Reemplaza con el nombre de tu procedimiento

    # Parámetros para el procedimiento (en este caso, solo el RUT)
    params = [ciudad]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return response, status_code

def obtener_parametros():
    package_name = "SGT.PCK_SGT"
    procedure_name = "SGTRECPARAMETRO"

    params = []

    response, status_code = funciones_db.pkg_exe_error_msg_cursor(procedure_name, package_name,params)


    return response, status_code

