import funciones_db
import datetime
from flask import current_app

def obtener_cuenta_ahorro(rut_titular,codigo_producto):
    """
    Servicio para obtener cuenta de ahorro
    """
    package_name = "AHORRO.PCK_AHORRO"
    procedure_name = "AhoRecCuentaAho"

    if not rut_titular and not codigo_producto :
        return "Faltan parámetros",400

    params = [rut_titular,codigo_producto]
    #current_app.logger.info(params)# Log de los params

    res = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    response , status_code = funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)

    current_app.logger.info(res)

    return response, status_code

def obtener_movimientos(codigo_cuenta,fecha_inicio,fecha_fin):
    """
    Servicio para obtener los movimientos de la cuenta de ahorro
    """
    package_name = "AHORRO.PCK_AHORRO"
    procedure_name = "RECUPERARMOVIMIENTOS"

    if not codigo_cuenta and not fecha_inicio and not fecha_fin :
        return "Faltan parámetros",400
    # Validación de formato de fechas
    
    #try:
    #    fecha_inicio = datetime.strptime(fecha_inicio,'%d-%m-%y')
    #    fecha_fin = datetime.strptime(fecha_fin,'%d-%m-%y')
    #except:
    #    current_app.logger.info(fecha_inicio)
    #    current_app.logger.info(fecha_fin)
    #    return "El formato de la fechas debe ser = 'dd-mm-yyyy'",400
    if fecha_inicio > fecha_fin:
        return "fechas incorrectas",400

    params = [codigo_cuenta,fecha_inicio,fecha_fin]
    current_app.logger.info(params)# Log de los params

    response , status_code = funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name,params)

    current_app.logger.info(response)

    return response, status_code

def verificar_existencia_bloqueo(rut):
    """
    Servicio para obtener los movimientos de la cuenta de ahorro
    """
    package_name = "AHORRO.PCK_AHORRO"
    procedure_name = "BloqDBFUAF_Final"

    if not rut :
        return "Faltan parámetros",400

    params = {
        "P_RUT":rut
    }

    response , status_code = funciones_db.pkg_exe_par_number(procedure_name,package_name,params)

    return response, status_code



