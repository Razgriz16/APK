from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import csocial_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g


repo = rp.CsocialRepository(funciones_db)

def obtener_cuenta_csocial(rut_titular):
    """
    Servicio para obtener cuenta de csocial
    """
    if not rut_titular:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'rut-titular' ", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuenta_csocial(rut_titular)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de csocial")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener cuenta de ahorro")

def obtener_ultimos_movimientos(cuenta,cantidad):
    if not cuenta and not cantidad :
        return {"error_code": 400, "error_message": "Faltan parámetros : 'cuenta' , 'cantidad' ", "trace_id": g.trace_id, "data": []}, 400

    if  not isinstance(cuenta,int):
        return {"error_code": 400, "error_message": "cuenta tiene que ser entero ", "trace_id": g.trace_id, "data": []}, 400

    if not isinstance(cantidad,int) or cantidad <= 0 :
        return {"error_code": 400, "error_message": "Cantidad tiene que ser mayor a 0 ", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_ultimos_movimientos(cuenta,cantidad)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener movimientos")

#def verificar_existencia_bloqueo(rut):
#    if not rut :
#        return {"error_code": 400, "error_message": "Faltan parámetros : 'rut'", "trace_id": g.trace_id, "data": []}, 400
#    try:
#        response,status_code = repo.verificar_existencia_bloqueo(rut)
#        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
#    except Exception as e :
#        return handle_service_error(e,context=f"Verifica bloqueo")
