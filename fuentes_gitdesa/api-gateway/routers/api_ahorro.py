from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request

ahorro_bp = Blueprint('ahorro',__name__,url_prefix="/v1/ahorro")


@ahorro_bp.route('/cuenta-ahorro')
@validar_rut(param_name='rut-titular')
@parse_query_params(
    rut_titular=int,
    codigo_producto=(int,0)
)
def obtener_cliente(rut_titular,codigo_producto):
    q=f"?rut-titular={rut_titular}&codigo-producto={codigo_producto}"
    return forward_request('ahorro',f"v1/cuenta-ahorro{q}")



@ahorro_bp.route('/cuenta-ahorro/movimientos')
@parse_query_params(
    numero_cuenta=int,
    fecha_inicio=(str,'0'),
    fecha_fin=(str,'0')
)
def obtener_movimientos(numero_cuenta,fecha_inicio,fecha_fin):
    q=f"?numero-cuenta={numero_cuenta}&fecha-inicio={fecha_inicio}&fecha-fin={fecha_fin}"
    return forward_request('ahorro',f"v1/cuenta-ahorro/movimientos")




@ahorro_bp.route('/cuenta-ahorro/cuenta/bloqueo-dbuaf')
@parse_query_params(
    rut=int
)
@validar_rut(param_name='rut')
def verificar_bloqueo_dbf_uaf(rut):
    q=f"?rut={rut}"
    return forward_request('ahorro',f"v1/cuenta-ahorro/cuenta/bloqueo-dbuaf{q}")




@ahorro_bp.route('/cuenta-ahorro/ultimos-movimientos')   
@parse_query_params(
    numero_cuenta=int,
    cantidad=(int,5)
)
def obtener_ultimos_movimientos(numero_cuenta,cantidad):
    q=f"?numero-cuenta={numero_cuenta}&cantidad={cantidad}"
    return forward_request('ahorro',f"v1/cuenta-ahorro/ultimos-movimientos{q}")
   

