import funciones_db
from flask import abort, render_template, current_app
from utils.jwt_utils import JWTManager
from utils.hash import verificar_password




def validar_respuesta(response,msg="Respuesta del servidor inválida"):
    """
    Valida la estructura de la respuesta y maneja errores comunes.

    Args:
        response (dict): Respuesta del servicio.

    Returns: tuple: Mensaje de error y código de estado, si corresponde.  """
    if not isinstance(response, dict) or "data" not in response:
        return {"error": msg}, 500

    if len(response["data"]) == 0:
        return {"error": "No se encontraron resultados"}, 404

    return None, None



def login(rut, clave):
    """
    Servicio iniciar sesion
    Args:
        rut: int
        clave: str
    Return: Si las credenciales son validas retorna access y refresh token
    """

    if not rut or not clave:
        return {"error":"Rut y Clave son requeridos"}, 400
    try:
        # Validar que existe un cliente con el rut que se paso
        response, status_code = obtener_rut_clave_usuario_por_rut(rut)
        error_response,error_code = validar_respuesta(response)
        if error_response:
            return error_response,error_code
        # Comparar passwords
        data = response["data"][0]
        clave_hasheada = data.get("clave")
        if not verificar_password(clave,clave_hasheada,rut):
            return {"error":"Credenciales incorrectas"},401

        # Crear accessToken
        jwt_manager = JWTManager()
        access_token = jwt_manager.generar_access_token(rut)
        refresh_token = jwt_manager.generar_refresh_token(rut)

        # Si tiene refreshToken eliminarlo
        # TODO
        # Guardar refreshToken en BD
        # TODO

        # return access y refreshToken
        return {
            "access_token": access_token,
            #"refresh_token": refresh_token,
        }, 200
    except Exception as e:
        # TODO: crear exception
        return {"error": str(e)}, 500


def get_usuario_por_rut(rut):
    """
    Servicio obtener informacion del cliente 
    Args:
        rut: int
    Return: Si las el run es valido retorna infromacio del cliente
    """

    if not rut:
        return {"error":"Rut es requerido"}, 400
    if not isinstance(rut,int):
        return {"error":"El rut es invalido"},400
    try:
        # Validar que existe un cliente con el rut 
        response, status_code = obtener_cliente(rut)
        error_response,error_code = validar_respuesta(response,"Rut invalido")
        if error_response:
            return error_response,error_code
        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        # TODO: crear exception
        return {"error": str(e)}, 500

def get_direccion_cliente(rut):
    """
    Servicio para obtener la dirección del cliente por RUT.
    Args:
        rut: int
    Return: Dirección del cliente si el RUT es válido.
    """
    if not rut:
        return {"error": "Rut es requerido"}, 400
    if not isinstance(rut, int):
        return {"error": "El RUT debe ser un número entero"}, 400

    try:
        response, status_code = obtener_direccion_por_rut(rut)
        error_response, error_code = validar_respuesta(response, "Dirección no encontrada")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500


def get_telefono_cliente(rut):
    """
    Servicio para obtener el teléfono del cliente por RUT.
    Args:
        rut: int
    Return: Teléfono del cliente si el RUT es válido.
    """
    if not rut:
        return {"error": "Rut es requerido"}, 400
    if not isinstance(rut, int):
        return {"error": "El RUT debe ser un número entero"}, 400

    try:
        response, status_code = obtener_telefono_por_rut(rut)
        error_response, error_code = validar_respuesta(response, "Teléfono no encontrado")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500

def get_telefono_verificado_cliente(rut):
    """
    Servicio para obtener el teléfono verificado del cliente por RUT.
    Args:
        rut: int
    Return: Teléfono verificado del cliente si el RUT es válido.
    """
    if not rut:
        return {"error": "Rut es requerido"}, 400
    if not isinstance(rut, int):
        return {"error": "El RUT debe ser un número entero"}, 400

    try:
        # Obtener el teléfono verificado del cliente
        response, status_code = obtener_telefono_verificado_por_rut(rut)
        if status_code != 200:
            return {"error": "Error al obtener el teléfono verificado"}, status_code

        return {
            "data": response,
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500


def get_telefono_verificado_cliente(rut):
    """
    Servicio para obtener el teléfono verificado del cliente por RUT.
    Args:
        rut: int
    Return: Teléfono verificado del cliente si el RUT es válido.
    """
    if not rut:
        return {"error": "Rut es requerido"}, 400
    if not isinstance(rut, int):
        return {"error": "El RUT debe ser un número entero"}, 400

    try:
        # Obtener el teléfono verificado del cliente
        response, status_code = obtener_telefono_verificado_por_rut(rut)
        if status_code != 200:
            return {"error": "Error al obtener el teléfono verificado"}, status_code

        return {
            "data": response,
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500

def get_correo_cliente(rut):
    """
    Servicio para obtener el correo del cliente por RUT.
    Args:
        rut: int
    Return: Correo del cliente si el RUT es válido.
    """
    if not rut:
        return {"error": "Rut es requerido"}, 400
    if not isinstance(rut, int):
        return {"error": "El RUT debe ser un número entero"}, 400

    try:
        # Obtener el correo del cliente
        response, status_code = obtener_correo_por_rut(rut)
        if status_code != 200:
            return {"error": "Error al obtener el correo"}, status_code

        return {
            "data": response,
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500

def get_sucursal_funcionario(usuario):
    """
    Servicio para obtener la sucursal del funcionario por usuario.
    Args:
        usuario: str
    Return: Sucursal del funcionario si el usuario es válido.
    """
    if not usuario:
        return {"error": "Usuario es requerido"}, 400
    if not isinstance(usuario, int):
        return {"error": "El usuario debe ser una cadena de texto"}, 400

    try:
        # Obtener la sucursal del funcionario
        response, status_code = obtener_sucursal_funcionario(usuario)
        if status_code != 200:
            return {"error": "Error al obtener la sucursal"}, status_code

        return {
            "data": response,
        }, 200
    except Exception as e:
        # TODO: Crear excepción personalizada
        return {"error": str(e)}, 500


#################################################
##  Funciones que interactuan con los packages ##
#################################################

def obtener_cliente(rut):
    """
    Servicio para obtener cliente
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="CliRecCliente"

    if not rut:
        return "Faltan parámetros",400

    params = [rut]

    #current_app.logger.info(params)
    #current_app.logger.info(credito)


    response , status_code = funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_rut_clave_usuario_por_rut(rut):
    """
    Servicio para rut y password del usuario 
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="CLIRECRUTPASSWORD"

    rut = int(rut)

    if not rut:
        return "Faltan parámetros",400
    if not isinstance(rut,int):
    	return "El run no es de tipo int",400 

    params = [rut]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code



def obtener_direccion_por_rut(rut):
    """
    Servicio para obtener direccion del cliente por rut
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="CLIRECDIRECCION"

    if not rut:
        return "Faltan parámetros",400

    params = [rut]

    response , status_code = funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)

    return response, status_code


def obtener_telefono_por_rut(rut):
    """
    Servicio para obtenerel telefono del cliente por rut
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="CLIRECTELEFONO"

    if not rut:
        return "Faltan parámetros",400

    params = [rut]

    response , status_code = funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_telefono_verificado_por_rut(rut):
    """
    Servicio para obtenerel telefono verificado del cliente por rut
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="cliRecTelefono_Verificado"

    if not rut:
        return "Faltan parámetros",400

    params = {
        "P_RUT":rut
    }

    response , status_code = funciones_db.pkg_exe_par_string(procedure_name,package_name,params)

    return response, status_code


def obtener_correo_por_rut(rut):
    """
    Servicio para obtener el correo  del cliente por rut
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="obtenerCorreoPorRut"

    if not rut:
        return "Faltan parámetros",400

    params = {
	"P_RUT":rut
    }

    response , status_code = funciones_db.pkg_exe_par_string(procedure_name,package_name,params)

    return response, status_code

def obtener_sucursal_funcionario(usuario):
    """
    Servicio para obtener el correo  del cliente por rut
    """
    package_name="CLIENTE.PCK_CLIENTE"
    procedure_name="RecuperarSucursalFuncionario"

    if not usuario:
        return "Faltan parámetros",400

    params = {
	"P_usuario":usuario
    }

    response , status_code = funciones_db.pkg_exe_par_string(procedure_name,package_name,params)

    return response, status_code

