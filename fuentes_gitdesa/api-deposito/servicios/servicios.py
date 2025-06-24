from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import dap_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g


repo = rp.DapRepository(funciones_db)

def recuperar_operaciones(rut_cliente, estado, fecha_inicio, fecha_fin, indicador1, indicador2):
    """
    Recupera operaciones en una coleccion
    Input args: rut_cliente: int, estado:int, fecha_inicio: string, fecha_fin: string, indicador1: string, indicador2: string
    """
    if any(x is None for x in (rut_cliente, estado, fecha_inicio, fecha_fin, indicador1, indicador2)):
        return {"error_code": 400, "error_message": "Faltan parámetros", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.recuperar_operaciones(rut_cliente, estado, fecha_inicio, fecha_fin, indicador1, indicador2)
        return procesar_respuesta_plsql(response,status_code,f"Obtener operaciones dap")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener operaciones dap")

