from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request



cr_bp = Blueprint('credito',__name__,url_prefix="/v1/credito/")

@cr_bp.route('/health')
def health():
    return forward_request('credito', 'v1/health')

@cr_bp.route('/creditos')#cambiar el @app.route por el cr_bp
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int,
    credito=(int,-1),
    estado=(int, -1),
    prorrogados=(str, 'N')
)
def obtener_credito(rut, credito, estado, prorrogados):
    q = f"?rut={rut}&credito={credito}&estado={estado}&prorrogados={prorrogados}"
    current_app.logger.info(q)
    return forward_request('credito', f"v1/creditos{q}")

@cr_bp.route('/creditos/bloqueo')
@parse_query_params(
    operacion=(int, None),
    estado=(str, '0'),
    judicial=(str, '0')
)
def obtener_credito_bloqueo(operacion, estado, judicial):
    q = f"?operacion={operacion}&estado={estado}&judicial={judicial}"
    return forward_request('credito', f"v1/creditos/bloqueo{q}")

@cr_bp.route('/creditos/cuotas')
@parse_query_params(
    operacion=(int, None),
    peso=(str, 'N')
)
def obtener_cuotas(operacion, peso):
    q = f"?operacion={operacion}&peso={peso}"
    return forward_request('credito', f"v1/creditos/cuotas{q}")

@cr_bp.route('/creditos/movimientos')
@parse_query_params(credito=(int, None))
def obtener_movimientos(credito):
    q = f"?credito={credito}"
    return forward_request('credito', f"v1/creditos/movimientos{q}")

@cr_bp.route('/operaciones/cliente')
@parse_query_params(
    todos=(str, None),
    fecha=(str, None),
    cliente=(int, 0),
    operacion=(int, 0)
)
def obtener_operaciones_cliente(todos, fecha, cliente, operacion):
    q = f"?todos={todos}&fecha={fecha}&cliente={cliente}&operacion={operacion}"
    return forward_request('credito', f"v1/operaciones/cliente{q}")

@cr_bp.route('/prorrogas/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/detalle{q}")

@cr_bp.route('/prorrogas/rechazos')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_rechazos_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/rechazos{q}")

@cr_bp.route('/prorrogas/cuotas')
@parse_query_params(
    convert_underscore=False,
    id_prorroga=int,
    cuota_desde=(int, None),
    cuota_hasta=(int, None)
)
def obtener_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta):
    q = f"?id_prorroga={id_prorroga}&cuota_desde={cuota_desde}&cuota_hasta={cuota_hasta}"
    #current_app.logger.info(q)
    return forward_request('credito', f"v1/prorrogas/cuotas{q}")

@cr_bp.route('/prorrogas/cuotas/posterior')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_cuotas_prorrogas_posterior(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cuotas/posterior{q}")

@cr_bp.route('/prorrogas/cuotas/posterior/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_cuotas_prorrogas_posterior(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cuotas/posterior/detalle{q}")

@cr_bp.route('/prorrogas/cargos')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_cargos_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cargos{q}")

@cr_bp.route('/prorrogas/creditos')
@validar_rut(param_name='rut')
@parse_query_params(rut=int)
def obtener_creditos_prorroga(rut):
    q = f"?rut={rut}"
    return forward_request('credito', f"v1/prorrogas/creditos{q}")

@cr_bp.route('/prorrogas/rechazos/usuario')
@parse_query_params(convert_underscore=False,id_prorroga=int, id_usuario=int)
def obtener_rechazo_prorroga_usuario(id_prorroga, id_usuario):
    q = f"?id_prorroga={id_prorroga}&id_usuario={id_usuario}"
    return forward_request('credito', f"v1/prorrogas/rechazos/usuario{q}")

@cr_bp.route('/parametros')
def obtener_parametros():
    return forward_request('credito', 'v1/parametros')

@cr_bp.route('/prorrogas/grupo')
@parse_query_params(codigo=(int, None))
def obtener_grupo_prorrogas(codigo):
    q = f"?codigo={codigo}"
    return forward_request('credito', f"v1/prorrogas/grupo{q}")

@cr_bp.route('/prorrogas/cuota/posterior/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_cuota_posterior_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cuota/posterior/detalle{q}")

@cr_bp.route('/prorrogas/cuota/anterior/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_cuota_anterior_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cuota/anterior/detalle{q}")

@cr_bp.route('/prorrogas/cargos/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_cargos_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/cargos/detalle{q}")

@cr_bp.route('/prorrogas/rechazos/detalle')
@parse_query_params(convert_underscore=False,id_prorroga=int)
def obtener_detalle_rechazos_prorroga(id_prorroga):
    q = f"?id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/rechazos/detalle{q}")

@cr_bp.route('/prorrogas/operaciones/cantidad')
@validar_rut(param_name='rut')
@parse_query_params(rut=int)
def obtener_cantidad_operaciones_prorrogas_por_rut(rut):
    q = f"?rut={rut}"
    return forward_request('credito', f"v1/prorrogas/operaciones/cantidad{q}")

@cr_bp.route('/operaciones/cantidad')
@validar_rut(param_name='rut')
@parse_query_params(rut=int)
def obtener_cantidad_operaciones_por_rut(rut):
    q = f"?rut={rut}"
    return forward_request('credito', f"v1/operaciones/cantidad{q}")

@cr_bp.route('/prorrogas/firmadas')
@parse_query_params(convert_underscore=False,id_usuario=int, id_prorroga=(int, -1))
def obtener_prorrogas_firmadas(id_usuario, id_prorroga):
    q = f"?id_usuario={id_usuario}&id_prorroga={id_prorroga}"
    return forward_request('credito', f"v1/prorrogas/firmadas{q}")

@cr_bp.route('/prorrogas/firmadas/todas')
def obtener_todas_prorrogas_firmadas():
    return forward_request('credito', 'v1/prorrogas/firmadas/todas')

@cr_bp.route('/prorrogas/firmas')
@parse_query_params(convert_underscore=False,id_usuario=int)
def obtener_prorrogas_firmas(id_usuario):
    q = f"?id_usuario={id_usuario}"
    return forward_request('credito', f"v1/prorrogas/firmas{q}")

@cr_bp.route('/prorrogas/firmas/todas')
def obtener_todas_prorrogas_firmas():
    return forward_request('credito', 'v1/prorrogas/firmas/todas')

@cr_bp.route('/prorrogas/existe')
@parse_query_params(operacion=int)
def validar_existencia_prorroga(operacion):
    q = f"?operacion={operacion}"
    return forward_request('credito', f"v1/prorrogas/existe{q}")
