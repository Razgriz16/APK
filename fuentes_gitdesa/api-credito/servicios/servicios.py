from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import credito_repo as rp
from utils.error_util import handle_service_error
import funciones_db
from flask import g


repo = rp.CreditoRepository(funciones_db)

def get_credito(credito, rut, estado=-1, prorrogados='N'):
    """
    Servicio para obtener crédito a partir de RUT y/o crédito.
    Args:
        credito: int
        rut: int
        estado: int (opcional, default=-1)
        prorrogados: str (opcional, default='N')
    Return: Datos del crédito si los parámetros son válidos.
    """
    if not credito and not rut:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'credito' o 'rut'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(rut,int) or not isinstance(credito,int):
        return {"error_code": 400, "error_message": "Credito y Rut tienen que ser enteros",
                "trace_id": g.trace_id, "data": []}, 400

    if prorrogados not in ['S', 'N']:
        return {"error_code": 400, "error_message": "Prorrogados puede ser 'S' o 'N'",
                "trace_id": g.trace_id, "data": []}, 400


    try:
        response, status_code = repo.obtener_credito(credito,rut,estado,prorrogados)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener credito")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion de credito")


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
        return {"error_code": 400, "error_message": "Faltan parámetros : 'operacion'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(operacion, int):
        return {"error_code": 400, "error_message": "Operacion tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_credito_bloqueo(operacion,estado,judicial) 
        return  procesar_respuesta_plsql(response,status_code,f"Obtener bloqueos de credito")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion de bloqueos de credito")

def get_cuotas(operacion, peso='N'):
    """
    Servicio para obtener cuotas de crédito.
    Args:
        operacion: int
        peso: str (opcional, default='N')
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not operacion:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'operacion'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(operacion, int):
        return {"error_code": 400, "error_message": "Operacion tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400
    if peso not in ['S', 'N']:
        return {"error_code": 400, "error_message": "Peso es invalido, los valores validos son :'S' y 'N'", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuotas(operacion,peso='N')
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cutoas de credito")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion de cuotas")

def obtener_movimientos(credito):
    """
    Servicio para obtener movimientos de crédito.
    Args:
        credito: int
    Return: Datos de los movimientos si los parámetros son válidos.
    """
    if not credito:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'credito'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(credito, int):
        return {"error_code": 400, "error_message": "Credito tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_movimientos(credito)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cutoas de credito")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion de movimientos")

def obtener_operaciones_cliente(todos, fecha, cliente=0, operacion=0):
    """
    Servicio para obtener operaciones de cliente.
    Args:
        todos: str
        fecha: str
        cliente: int (opcional, default=0)
        operacion: int (opcional, default=0)
    Return: Datos de las operaciones si los parámetros son válidos.
    """
    if not fecha or todos:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'credito' o 'todos'", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_operaciones_cliente(todos,fecha,cliente,operacion)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener operaciones del cliente")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion de las operaciones del cliente")

def obtener_detalle_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de prórroga si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_prorroga(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener detalle de prorroga")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion del detalle de prorroga")

def get_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener rechazos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los rechazos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_rechazos_prorroga(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener detalle de rechazos prorroga")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion del detalle de rechazos de  prorroga")

def get_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta):
    """
    Servicio para obtener cuotas de prórrogas.
    Args:
        id_prorroga: int
        cuota_desde: int
        cuota_hasta: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga or not cuota_desde or not cuota_hasta:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga' o 'cuota_desde' o 'cuota_hasta'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int) or not isinstance(cuota_desde, int) or not isinstance(cuota_hasta, int):
        return {"error_code": 400, "error_message": "id_prorroga , cuota_desde y cuota_hasta tienen que ser enteros", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cuotas prorrogadas")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion detalle de cuotas prorrogadas")

def get_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuotas_prorrogas_posterior(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cuotas posterior")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion detalle de cuotas posterior")

def get_detalle_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_cuotas_prorrogas_posterior(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener detalle de cutoas prorrogadas posterior")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion detalle de cuotas prorrogadas")

def get_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cargos_prorroga(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cargos de prorroga")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener informacion detalle de cuotas prorrogadas")



def get_creditos_prorroga(rut):
    """
    Servicio para obtener créditos de prórroga.
    Args:
        rut: int
    Return: Datos de los créditos si los parámetros son válidos.
    """
    if not rut:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'rut'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "rut tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_creditos_prorroga(rut)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener creditos de prorroga")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener creditos de prorroga")


def get_rechazo_prorroga_usuario(id_prorroga, id_usuario):
    """
    Servicio para obtener rechazo de prórroga por usuario.
    Args:
        id_prorroga: int
        id_usuario: int
    Return: Datos del rechazo si los parámetros son válidos.
    """
    if not id_prorroga or not id_usuario:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorrogas' o 'id_usuario'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int) or not isinstance(id_usuario, int):
        return {"error_code": 400, "error_message": "Los valores de 'id_prorrogas' o 'id_usuario' tienen que ser enteros", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_rechazo_prorroga_usuario(id_prorroga, id_usuario)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener rechazo de prorrogas del usuario")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener rechazos de prorrogas de usuario")

def get_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta):
    """
    Servicio para obtener cuotas de prórrogas.
    Args:
        id_prorroga: int
        cuota_desde: int
        cuota_hasta: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga or not cuota_desde or not cuota_hasta:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorrogas' o 'cuota_desde' o 'cuota_hasta'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int) or not isinstance(cuota_desde, int) or not isinstance(cuota_hasta, int):
        return {"error_code": 400, "error_message": "Los parametros id_prorroga, cuota_desde y cuota_hasta tienen que ser enteros", "trace_id": g.trace_id, "data": []}, 400
    try:
        response, status_code = repo.obtener_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cuotas de prorrogas")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener cuotas de prorrogas")

def get_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorrogas'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cuotas_prorrogas_posterior(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener cuotas de prorrogas posterior")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener cuotas de prorrogas posterior")


def get_detalle_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros : 'id_prorrogas'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "id_prorroga tiene que ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_cuotas_prorrogas_posterior(id_prorroga)
        return  procesar_respuesta_plsql(response,status_code,f"Obtener detalle de cuotas de prorrogas posterior")
    except Exception as e:
        return handle_service_error(e,context=f"Obtener detalles de cuotas de prorrogas posterior")

def get_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cargos_prorroga(id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener cargos de prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de cargos de prórroga")


def get_creditos_prorroga(rut):
    """
    Servicio para obtener créditos de prórroga.
    Args:
        rut: int
    Return: Datos de los créditos si los parámetros son válidos.
    """
    if not rut:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'rut'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El parámetro 'rut' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_creditos_prorroga(rut)
        return procesar_respuesta_plsql(response, status_code, "Obtener créditos de prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de créditos de prórroga")



def get_rechazo_prorroga_usuario(id_prorroga, id_usuario):
    """
    Servicio para obtener rechazo de prórroga por usuario.
    Args:
        id_prorroga: int
        id_usuario: int
    Return: Datos del rechazo si los parámetros son válidos.
    """
    if not id_prorroga or not id_usuario:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga' o 'id_usuario'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int) or not isinstance(id_usuario, int):
        return {"error_code": 400, "error_message": "Los parámetros deben ser enteros", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_rechazo_prorroga_usuario(id_prorroga, id_usuario)
        return procesar_respuesta_plsql(response, status_code, "Obtener rechazo de prórroga por usuario")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de rechazo de prórroga por usuario")


def get_parametros():
    """
    Servicio para obtener parámetros.
    Return: Datos de los parámetros si la operación es válida.
    """
    try:
        response, status_code = repo.obtener_parametros()
        return procesar_respuesta_plsql(response, status_code, "Obtener parámetros")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de parámetros")


def get_grupo_prorrogas(codigo):
    """
    Servicio para obtener parámetros de grupos de prórrogas.
    Args:
        codigo: int
    Return: Datos del grupo de prórrogas si los parámetros son válidos.
    """
    if not codigo:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'codigo'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(codigo, int):
        return {"error_code": 400, "error_message": "El parámetro 'codigo' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_grupo_prorrogas(codigo)
        return procesar_respuesta_plsql(response, status_code, "Obtener grupo de prórrogas")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de grupo de prórrogas")


def get_detalle_cuota_posterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de la prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_cuota_posterior_prorroga(id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener detalle de cuotas posteriores de la prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de detalle de cuotas posteriores de la prórroga")


def get_detalle_cuota_anterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cuotas anteriores de la prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_cuota_anterior_prorroga(id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener detalle de cuotas anteriores de la prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener informacón de detalle de cuotas anteriores de la prórroga")


def get_detalle_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_cargos_prorroga(id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener detalle de cargos de prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de detalle de cargos de prórroga")


def get_detalle_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de rechazos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de rechazos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_prorroga'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_detalle_rechazos_prorroga(id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener detalle de rechazos de prórroga")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de detalle de rechazos de prórroga")


def get_cantidad_operaciones_prorrogas_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones prorrogadas por RUT.
    Args:
        rut: int
    Return: Cantidad de operaciones si los parámetros son válidos.
    """
    if not rut:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'rut'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El parámetro 'rut' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cantidad_operaciones_prorrogas_por_rut(rut)
        return procesar_respuesta_plsql(response, status_code, "Obtener cantidad de operaciones prorrogadas por RUT")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de cantidad de operaciones prorrogadas por RUT")


def get_cantidad_operaciones_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones por RUT.
    Args:
        rut: int
    Return: Cantidad de operaciones si los parámetros son válidos.
    """
    if not rut:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'rut'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El parámetro 'rut' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_cantidad_operaciones_por_rut(rut)
        return procesar_respuesta_plsql(response, status_code, "Obtener cantidad de operaciones por RUT")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de cantidad de operaciones por RUT")


def get_prorrogas_firmadas(id_usuario, id_prorroga=-1):
    """
    Servicio para obtener las prórrogas firmadas.
    Args:
        id_usuario: int
        id_prorroga: int (opcional, default=-1)
    Return: Datos de las prórrogas firmadas si los parámetros son válidos.
    """
    if not id_usuario:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_usuario'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_usuario, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_usuario' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400
    if id_prorroga != -1 and not isinstance(id_prorroga, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_prorroga' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_prorrogas_firmadas(id_usuario, id_prorroga)
        return procesar_respuesta_plsql(response, status_code, "Obtener prórrogas firmadas")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de prórrogas firmadas")


def get_todas_prorrogas_firmadas():
    """
    Servicio para obtener todas las prórrogas firmadas.
    Return: Datos de todas las prórrogas firmadas si la operación es válida.
    """
    try:
        response, status_code = repo.obtener_todas_prorrogas_firmadas()
        return procesar_respuesta_plsql(response, status_code, "Obtener todas las prórrogas firmadas")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de todas las prórrogas firmadas")


def get_prorrogas_firmas(id_usuario):
    """
    Servicio para obtener prorrogas firmas del usuario.
    Args:
        id_usuario: int
    Return: Datos de todas las prórrogas del usuario.
    """
    if not id_usuario:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'id_usuario'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(id_usuario, int):
        return {"error_code": 400, "error_message": "El parámetro 'id_usuario' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.obtener_prorrogas_firmas(id_usuario)
        return procesar_respuesta_plsql(response, status_code, "Obtener prorrogas firmas del usuario")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de prorrogas firmas del usuario")


def get_todas_prorrogas_firmas():
    """
    Servicio para obtener todas las prórrogas del usuario.
    Return: Datos de todas las prórrogas del usuario.
    """
    try:
        response, status_code = repo.obtener_todas_prorrogas_firmas()
        return procesar_respuesta_plsql(response, status_code, "Obtener todas las prórrogas del usuario")
    except Exception as e:
        return handle_service_error(e, context="Obtener información de todas las prórrogas del usuario")


def get_validar_prorroga(operacion):
    """
    Servicio para validar existencia de prórroga a partir de operación.
    Args:
        operacion: int
    Return: Datos de la prórroga.
    """
    if not operacion:
        return {"error_code": 400, "error_message": "Faltan parámetros: 'operacion'", "trace_id": g.trace_id, "data": []}, 400
    if not isinstance(operacion, int):
        return {"error_code": 400, "error_message": "El parámetro 'operacion' debe ser un entero", "trace_id": g.trace_id, "data": []}, 400

    try:
        response, status_code = repo.validar_existencia_prorroga(operacion)
        return procesar_respuesta_plsql(response, status_code, "Validar existencia de prórroga")
    except Exception as e:
        return handle_service_error(e, context="Validar existencia de prórroga")

