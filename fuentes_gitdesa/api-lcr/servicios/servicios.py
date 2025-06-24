from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import lcr_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g

repo = rp.LcrRepository(funciones_db)



def get_lineacr(rut):
    """
    Servicio para obtener lineacr
    Args:
        rut: int
    Return: Datos de lineacr
    """
    if not rut:
        return {"error_code":400,"error_message": "Faltan parámetros: 'rut'","trace_id":g.trace_id,"data":[]}, 400
    if not isinstance(rut,int):
        return {"error_code":400,"error_message": "Rut tiene que ser entero","trace_id":g.trace_id,"data":[]}, 400

    try:
        response, status_code = repo.get_lineacr(rut)
        return procesar_respuesta_plsql(response,status_code,f"Obtener lineacr por rut")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener lcc por rut")

def get_mov_lineacr(nro_cuenta, cantidad):
    """
    Servicio para obtener movimientos lineacr
    Args:
        nro_cuenta: int
	cantidad: int
    Return: Datos de lineacr
    """
    if not nro_cuenta:
        return {"error_code":400,"error_message": "Faltan parámetros: 'nro_cuenta'","trace_id":g.trace_id,"data":[]}, 400
    if not isinstance(nro_cuenta,int):
        return {"error_code":400,"error_message": "nro_cuenta tiene que ser entero","trace_id":g.trace_id,"data":[]}, 400

    try:
        response, status_code = repo.get_mov_lineacr(nro_cuenta, cantidad)
        return procesar_respuesta_plsql(response,status_code,f"Obtener movimientos lineacr por numero de cuenta")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener movimientos lcc por numero de cuenta")
