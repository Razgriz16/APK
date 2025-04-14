import funciones_db
from flask import current_app


def obtener_usuario(identificador):
    """
    Servicio para obtener usuario a partir de su identificado
    :param:
    :identificador: int
    """

    package_name="HERMES.PCK_HERMES"
    procedure_name="HRMRECUSUARIO"
    if not identificador:
        return "Faltan parámetros",400
    if not isinstance(identificador,int):
        return "Parametros incorrectos",400


    params = [identificador]
    current_app.logger.info(params) #Log de params

    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
   
    return response,status_code


def obtener_privilegios_usuario(identificador,sistema):
    """
    Servicio para obtener los privilegios del usuario
    :param:
    :identificador: int
    :sistema: int
    """

    package_name="HERMES.PCK_HERMES"
    procedure_name="HRMRECPRIVILEGIOUSUARIO"
    if not identificador or not sistema:
        return "Faltan parámetros",400

    if not isinstance(identificador,int):
        return "Parametros incorrectos",400

    if not isinstance(sistema,int):
        return "Parametros incorrectos",400


    params = [identificador,sistema]
    current_app.logger.info(params) #Log de params

    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
   
    return response,status_code

def obtener_usuario_accion(accion,sistema):
    """
    Servicio para obtener los usuarios por accion y sistema
    :param:
    :accion: int
    :sistema: int
    """

    package_name="HERMES.PCK_HERMES"
    procedure_name="HRMRECUSUARIOSCONPRIVILEGIO"
    if not accion or not sistema:
        return "Faltan parámetros",400

    if not isinstance(accion,int):
        return "Parametros incorrectos",400

    if not isinstance(sistema,int):
        return "Parametros incorrectos",400


    params = [accion,sistema]
    current_app.logger.info(params) #Log de params

    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
   
    return response,status_code

def obtener_acciones_usuario(idusuario,accion):
    """
    Servicio para obtener las acciones de un usuario
    :param:
    :idusuario: int
    :accion: int
    """

    package_name="HERMES.PCK_HERMES"
    procedure_name="HRMVALIDAACCION"


    if not accion or not idusuario:
        return "Faltan parámetros",400

    if not isinstance(accion,int):
        return "Parametros incorrectos",400

    if not isinstance(idusuario,int):
        return "Parametros incorrectos",400


    params = [idusuario,accion]
    current_app.logger.info(params) #Log de params

    response, status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
   
    return response,status_code



