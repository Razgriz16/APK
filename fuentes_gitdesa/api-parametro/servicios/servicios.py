from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import parametros_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g

repo = rp.ParametrosRepository(funciones_db)

def get_sucursales_activas():
    """
    Servicio obtener las sucursales activas
    Args:
        None
    Return: Devuelve las sucursales activas
    """
    try:
        response, status_code = repo.recuperar_sucursales_activas()
        return procesar_respuesta_plsql(response, status_code, "Obtener sucursales activas")
    except Exception as e:
        return handle_service_error(e, context="Obtener sucursales activas")

def get_sucursal_por_codigo(codigo):
    """
    Servicio obtener sucursal por codigo
    Args:
        codigo:int
    Return: Si el codigo es valido devuelve la sucursal
    """
    if not codigo:
        return {"error_code": 400, "error_message": "Faltan parámetros", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(codigo,int):
        return {"error_code": 400, "error_message": "Código de sucursal tiene que ser enteros", 
                "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_sucursal(codigo)
        return procesar_respuesta_plsql(response, status_code, f"Obtener sucursal por código {codigo}")
    except Exception as e:
        return handle_service_error(e, context=f"Obtener sucursal por código {codigo}")

def get_comunas(comuna=-1, ciudad=-1):
    """
    Servicio obtener las comunas
    Args:
        comuna:int
        ciudad:int
    Return: retorna informacion de la comuna/s
    """
    if not isinstance(comuna, int) or not isinstance(ciudad, int):
        return {"error_code": 400, "error_message": "Código ciudad y código comuna tienen que ser enteros", 
                "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_comunas(comuna, ciudad)
        return procesar_respuesta_plsql(response, status_code, f"Obtener comunas (comuna={comuna}, ciudad={ciudad})")
    except Exception as e:
        return handle_service_error(e, context=f"Obtener comunas (comuna={comuna}, ciudad={ciudad})")

def get_ciudades(ciudad=-1):
    """
    Servicio obtener las ciudades
    Args:
        ciudad:int
    Return: retorna informacion de la ciudad/es
    """
    try:
        response, status_code = repo.obtener_ciudades(ciudad)
        return procesar_respuesta_plsql(response, status_code, f"Obtener ciudades (ciudad={ciudad})")
    except Exception as e:
        return handle_service_error(e, context=f"Obtener ciudades (ciudad={ciudad})")

def get_parametros_sgt():
    """
    Servicio obtener los parámetros SGT
    Args:
        None
    Return: retorna información de los parámetros
    """
    try:
        response, status_code = repo.obtener_parametros()
        return procesar_respuesta_plsql(response, status_code, "Obtener parámetros SGT")
    except Exception as e:
        return handle_service_error(e, context="Obtener parámetros SGT")

def get_credito_bloqueo(operacion, estado='0', judicial='0'):
    """
    Servicio para obtener bloqueos de crédito.
    Args:
        operacion: int
        estado: str (opcional, default='0')
        judicial: str (opcional, default='0')
    Return: Datos del bloqueo de crédito si los parámetros son válidos.
    """
    if not operacion:
        return {"error": "Faltan parámetros: 'operacion'"}, 400
    if not isinstance(operacion, int):
        return {"error": "El parámetro 'operacion' debe ser un entero"}, 400

    try:
        response, status_code = repo.obtener_credito_bloqueo(operacion,estado,judicial)
        return procesar_respuesta_plsql(response, status_code, "Obtener bloqueos de credito")

    except Exception as e:
        return handle_service_error(e,context="Obtener bloques de credito")

def get_cliente(rut):
    """
    Servicio para obtener bloqueos de crédito.
    Args:
        operacion: int
        estado: str (opcional, default='0')
        judicial: str (opcional, default='0')
    Return: Datos del bloqueo de crédito si los parámetros son válidos.
    """
    if not rut:
        return {"error": "Faltan parámetros: 'operacion'"}, 400
    if not isinstance(rut, int):
        return {"error": "El parámetro 'operacion' debe ser un entero"}, 400

    try:
        response, status_code = repo.obtener_cliente(rut)
        return procesar_respuesta_plsql(response, status_code, "Obtener datos del cliente")

    except Exception as e:
        return handle_service_error(e,context="Obtener datos del cliente")

