from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request

lcr_bp = Blueprint("lcr",__name__, url_prefix="/v1/lcr")
#test

@lcr_bp.route('/lineacr',methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_lineacr(rut):
    q=f"?rut={rut}"
    return forward_request('lineacr',f"v1/lineacr{q}")

@lcr_bp.route('/lineacr/movimientos',methods=['GET'])
@parse_query_params(
    nro_cuenta=int,
    cantidad = int
)
def obtener_mov_lineacr(nro_cuenta, cantidad):
    numero_cuenta=f"?numero-cuenta={nro_cuenta}&cantidad={cantidad}"
    return forward_request('lineacr',f"v1/lineacr/movimientos{numero_cuenta}")
