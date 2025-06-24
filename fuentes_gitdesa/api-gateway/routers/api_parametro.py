from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request


par_bp = Blueprint('parametro',__name__,url_prefix="/v1/parametro")

@par_bp.route('/sucursales/activas', methods=['GET'])
def obtener_sucursales_activas():
    return forward_request('parametro',f"v1/sucursales/activas")

@par_bp.route('/sucursal', methods=['GET'])
@parse_query_params(
    codigo=int
)
def obtener_sucursal_por_codigo(codigo):
    q = f"?codigo={codigo}"
    return forward_request('parametro',f"v1/sucursal{q}")

@par_bp.route('/comunas', methods=['GET'])
@parse_query_params(
    comuna=(int, -1),
    ciudad=(int, -1),
)
def obtener_comunas(comuna,ciudad):
    q = f"?comuna={comuna}&ciudad={ciudad}"
    return forward_request('parametro',f"v1/comunas{q}")

@par_bp.route('/ciudades', methods=['GET'])
@parse_query_params(
    ciudad=(int, -1)
)
def obtener_ciudades(ciudad):
    q = f"?ciudad={ciudad}"
    return forward_request('parametro',f"v1/ciudades{q}")

@par_bp.route('/parametros-sgt', methods=['GET'])
def obtener_parametros_sgt():
    return forward_request('parametro',f"v1/parametros-sgt")
