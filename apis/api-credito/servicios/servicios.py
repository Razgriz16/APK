import funciones_db
from flask import abort, render_template, current_app
from repositorios import repositorios as rp


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



def get_credito(credito, rut, estado=-1, prorrogados='N'):
    """
    Servicio para obtener crédito a partir de RUT y/o crédito.
    Args:
        credito: int (opcional)
        rut: int (opcional)
        estado: int (opcional, default=-1)
        prorrogados: str (opcional, default='N')
    Return: Datos del crédito si los parámetros son válidos.
    """
    if not credito and not rut:
        return {"error": "Faltan parámetros: 'credito' o 'rut'"}, 400
    if prorrogados not in ['S', 'N']:
        return {"error": "El parámetro para 'prorrogados' debe ser 'S' o 'N'"}, 400

    try:
        response, status_code = rp.obtener_credito(credito,rut,estado,prorrogados)
        error_response, error_code = validar_respuesta(response, "Error al obtener crédito")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


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
        response, status_code = rp.obtener_credito_bloqueo(operacion,estado,judicial) 
        error_response, error_code = validar_respuesta(response, "Error al obtener bloqueo de crédito")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_cuotas(operacion, peso='N'):
    """
    Servicio para obtener cuotas de crédito.
    Args:
        operacion: int
        peso: str (opcional, default='N')
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not operacion:
        return {"error": "Faltan parámetros: 'operacion'"}, 400
    if not isinstance(operacion, int):
        return {"error": "El parámetro 'operacion' debe ser un entero"}, 400
    if peso not in ['S', 'N']:
        return {"error": "El parámetro para 'peso' debe ser 'S' o 'N'"}, 400

    try:
        response, status_code = rp.obtener_cuotas(operacion,peso='N')
        error_response, error_code = validar_respuesta(response, "Error al obtener cuotas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def obtener_movimientos(credito):
    """
    Servicio para obtener movimientos de crédito.
    Args:
        credito: int
    Return: Datos de los movimientos si los parámetros son válidos.
    """
    if not credito:
        return {"error": "Faltan parámetros: 'credito'"}, 400
    if not isinstance(credito, int):
        return {"error": "El parámetro 'credito' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_movimientos(credito)
        error_response, error_code = validar_respuesta(response, "Error al obtener movimientos")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

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
    if not fecha:
        return {"error": "Faltan parámetros: 'fecha'"}, 400

    try:
        response, status_code = rp.obtener_operaciones_cliente(todos,fecha,cliente,operacion)
        error_response, error_code = validar_respuesta(response, "Error al obtener operaciones de cliente")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def obtener_detalle_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de prórroga si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener rechazos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los rechazos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_rechazos_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener rechazos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

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
        return {"error": "Faltan parámetros: 'id_prorroga', 'cuota_desde', 'cuota_hasta'"}, 400
    if not isinstance(id_prorroga, int) or not isinstance(cuota_desde, int) or not isinstance(cuota_hasta, int):
        return {"error": "Los parámetros deben ser enteros"}, 400

    try:
        response, status_code = rp.obtener_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
        error_response, error_code = validar_respuesta(response, "Error al obtener cuotas de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cuotas_prorrogas_posterior(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener cuotas posteriores de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_detalle_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_cuotas_prorrogas_posterior(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de cuotas posteriores de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cargos_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener cargos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500



def get_creditos_prorroga(rut):
    """
    Servicio para obtener créditos de prórroga.
    Args:
        rut: int
    Return: Datos de los créditos si los parámetros son válidos.
    """
    if not rut:
        return {"error": "Faltan parámetros: 'rut'"}, 400
    if not isinstance(rut, int):
        return {"error": "El parámetro 'rut' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_creditos_prorroga(rut)
        error_response, error_code = validar_respuesta(response, "Error al obtener créditos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_rechazo_prorroga_usuario(id_prorroga, id_usuario):
    """
    Servicio para obtener rechazo de prórroga por usuario.
    Args:
        id_prorroga: int
        id_usuario: int
    Return: Datos del rechazo si los parámetros son válidos.
    """
    if not id_prorroga or not id_usuario:
        return {"error": "Faltan parámetros: 'id_prorroga' o 'id_usuario'"}, 400
    if not isinstance(id_prorroga, int) or not isinstance(id_usuario, int):
        return {"error": "Los parámetros deben ser enteros"}, 400

    try:
        response, status_code = rp.obtener_rechazo_prorroga_usuario(id_prorroga, id_usuario)
        error_response, error_code = validar_respuesta(response, "Error al obtener rechazo de prórroga por usuario")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

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
        return {"error": "Faltan parámetros: 'id_prorroga', 'cuota_desde', 'cuota_hasta'"}, 400
    if not isinstance(id_prorroga, int) or not isinstance(cuota_desde, int) or not isinstance(cuota_hasta, int):
        return {"error": "Los parámetros deben ser enteros"}, 400

    try:
        response, status_code = rp.obtener_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
        error_response, error_code = validar_respuesta(response, "Error al obtener cuotas de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos de las cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cuotas_prorrogas_posterior(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener cuotas posteriores de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_detalle_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de prórrogas.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_cuotas_prorrogas_posterior(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de cuotas posteriores de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos de los cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cargos_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener cargos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_creditos_prorroga(rut):
    """
    Servicio para obtener créditos de prórroga.
    Args:
        rut: int
    Return: Datos de los créditos si los parámetros son válidos.
    """
    if not rut:
        return {"error": "Faltan parámetros: 'rut'"}, 400
    if not isinstance(rut, int):
        return {"error": "El parámetro 'rut' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_creditos_prorroga(rut)
        error_response, error_code = validar_respuesta(response, "Error al obtener créditos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_rechazo_prorroga_usuario(id_prorroga, id_usuario):
    """
    Servicio para obtener rechazo de prórroga por usuario.
    Args:
        id_prorroga: int
        id_usuario: int
    Return: Datos del rechazo si los parámetros son válidos.
    """
    if not id_prorroga or not id_usuario:
        return {"error": "Faltan parámetros: 'id_prorroga' o 'id_usuario'"}, 400
    if not isinstance(id_prorroga, int) or not isinstance(id_usuario, int):
        return {"error": "Los parámetros deben ser enteros"}, 400

    try:
        response, status_code = rp.obtener_rechazo_prorroga_usuario(id_prorroga, id_usuario)
        error_response, error_code = validar_respuesta(response, "Error al obtener rechazo de prórroga por usuario")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


#TODO: hacer el get_linea_credito
def get_parametros():
    """
    Servicio para obtener parámetros.
    Return: Datos de los parámetros si la operación es válida.
    """
    try:
        response, status_code = rp.obtener_parametros()
        error_response, error_code = validar_respuesta(response, "Error al obtener parámetros")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_grupo_prorrogas(codigo):
    """
    Servicio para obtener parámetros de grupos de prórrogas.
    Args:
        codigo: int
    Return: Datos del grupo de prórrogas si los parámetros son válidos.
    """
    if not codigo:
        return {"error": "Faltan parámetros: 'codigo'"}, 400
    if not isinstance(codigo, int):
        return {"error": "El parámetro 'codigo' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_grupo_prorrogas(codigo)
        error_response, error_code = validar_respuesta(response, "Error al obtener grupo de prórrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500



def get_detalle_cuota_posterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cuotas posteriores de la prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_cuota_posterior_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de cuotas posteriores")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_detalle_cuota_anterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cuotas anteriores de la prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cuotas si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_cuota_anterior_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de cuotas anteriores")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500



def get_detalle_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de cargos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de cargos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_cargos_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de cargos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_detalle_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de rechazos de prórroga.
    Args:
        id_prorroga: int
    Return: Datos del detalle de rechazos si los parámetros son válidos.
    """
    if not id_prorroga:
        return {"error": "Faltan parámetros: 'id_prorroga'"}, 400
    if not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_detalle_rechazos_prorroga(id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener detalle de rechazos de prórroga")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_cantidad_operaciones_prorrogas_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones prorrogadas por RUT.
    Args:
        rut: int
    Return: Cantidad de operaciones si los parámetros son válidos.
    """
    if not rut:
        return {"error": "Faltan parámetros: 'rut'"}, 400
    if not isinstance(rut, int):
        return {"error": "El parámetro 'rut' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cantidad_operaciones_prorrogas_por_rut(rut)
        error_response, error_code = validar_respuesta(response, "Error al obtener cantidad de operaciones prorrogadas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500




def get_cantidad_operaciones_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones por RUT.
    Args:
        rut: int
    Return: Cantidad de operaciones si los parámetros son válidos.
    """
    if not rut:
        return {"error": "Faltan parámetros: 'rut'"}, 400
    if not isinstance(rut, int):
        return {"error": "El parámetro 'rut' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_cantidad_operaciones_por_rut(rut)
        error_response, error_code = validar_respuesta(response, "Error al obtener cantidad de operaciones")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_prorrogas_firmadas(id_usuario, id_prorroga=-1):
    """
    Servicio para obtener las prórrogas firmadas.
    Args:
        id_usuario: int
        id_prorroga: int (opcional, default=-1)
    Return: Datos de las prórrogas firmadas si los parámetros son válidos.
    """
    if not id_usuario:
        return {"error": "Faltan parámetros: 'id_usuario'"}, 400
    if not isinstance(id_usuario, int):
        return {"error": "El parámetro 'id_usuario' debe ser un entero"}, 400
    if id_prorroga != -1 and not isinstance(id_prorroga, int):
        return {"error": "El parámetro 'id_prorroga' debe ser un entero"}, 400

    try:
        response, status_code = rp.obtener_prorrogas_firmadas(id_usuario, id_prorroga)
        error_response, error_code = validar_respuesta(response, "Error al obtener prórrogas firmadas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_todas_prorrogas_firmadas():
    """
    Servicio para obtener todas las prórrogas firmadas.
    Return: Datos de todas las prórrogas firmadas si la operación es válida.
    """
    try:
        response, status_code = rp.obtener_todas_prorrogas_firmadas()
        error_response, error_code = validar_respuesta(response, "Error al obtener todas las prórrogas firmadas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_prorrogas_firmas(id_usuario):
    """
    Servicio para obtener prorrogas firmas del usuario
    Return: Datos de todas las prórrogas del usuario
    """
    if not id_usuario:
        return "Faltan parámetros : 'idusuario'",400
    if not isinstance(id_usuario,int):
        return "Parametro < idusuario > tiene que ser un entero",400

    try:
        response, status_code = rp.obtener_prorrogas_firmas(id_usuario)
        error_response, error_code = validar_respuesta(response, "Error al obtener todas prorrogas del usuario")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


def get_todas_prorrogas_firmas():
    """
    Servicio para obtener todas la prorrogas del usuario
    Return: Datos de todas las prórrogas del usuario
    """
    try:
        response, status_code = rp.obtener_todas_prorrogas_firmas()
        error_response, error_code = validar_respuesta(response, "Error al obtener todas prorrogas")
        if error_response:
            return error_response, error_code

        return {
            "data": response["data"],
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

