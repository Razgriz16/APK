from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import lcc_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g

repo = rp.LccRepository(funciones_db)



def get_lineacc(rut):
    """
    Servicio para obtener lineacc
    Args:
        rut: int
    Return: Datos de lineacc
    """
    if not rut:
        return {"error_code":400,"error_message": "Faltan parámetros: 'rut'","trace_id":g.trace_id,"data":[]}, 400
    if not isinstance(rut,int):
        return {"error_code":400,"error_message": "Rut tiene que ser entero","trace_id":g.trace_id,"data":[]}, 400

    try:
        response, status_code = repo.get_lineacc(rut)
        return procesar_respuesta_plsql(response,status_code,f"Obtener lineacc por rut")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener lcc por rut")
