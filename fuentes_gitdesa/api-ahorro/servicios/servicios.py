from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import ahorro_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g


repo = rp.CtaAhorroRepository(funciones_db)

def obtener_cuenta_ahorro(rut_titular,codigo_producto=0):
    """
    Servicio para obtener cuenta de ahorro
    """
    if not rut_titular and not codigo_producto :
        return {"error_code": 400, "error_message": "Faltan parámetros : 'rut_titular' o 'codigo_producto'", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuenta_ahorro(rut_titular,codigo_producto)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener cuenta de ahorro")

def obtener_movimientos(codigo_cuenta,fecha_inicio,fecha_fin):
    if not codigo_cuenta and not fecha_inicio and not fecha_fin :
        return {"error_code": 400, "error_message": "Faltan parámetros : 'codigo_cuenta' , 'fecha_inicio' o 'fecha_fin'", "trace_id": g.trace_id, "data": []}, 400

    if fecha_inicio > fecha_fin:
        return {"error_code": 400, "error_message": "Error en parametros : Fecha inicio o Fecha fin incorrectas", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_movimientos(codigo_cuenta,fecha_inicio,fecha_fin)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener movimientos")

def obtener_ultimos_movimientos(codigo_cuenta,cantidad):
    if not codigo_cuenta and not cantidad :
        return {"error_code": 400, "error_message": "Faltan parámetros : 'codigo_cuenta' , 'cantidad' ", "trace_id": g.trace_id, "data": []}, 400

    if  not isinstance(codigo_cuenta,int):
        return {"error_code": 400, "error_message": "Codigo cuenta tiene que ser entero ", "trace_id": g.trace_id, "data": []}, 400

    if not isinstance(cantidad,int) or cantidad <= 0 :
        return {"error_code": 400, "error_message": "Cantidad tiene que ser mayor a 0 ", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_ultimos_movimientos(codigo_cuenta,cantidad)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener movimientos")

def verificar_existencia_bloqueo(rut):
    if not rut :
        return {"error_code": 400, "error_message": "Faltan parámetros : 'rut'", "trace_id": g.trace_id, "data": []}, 400
    try:
        response,status_code = repo.verificar_existencia_bloqueo(rut)
        return procesar_respuesta_plsql(response,status_code,f"Obtener cuenta de ahorro")
    except Exception as e :
        return handle_service_error(e,context=f"Verifica bloqueo")
