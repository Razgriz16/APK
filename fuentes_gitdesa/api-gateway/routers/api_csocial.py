from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request

csocial_bp = Blueprint("csocial",__name__, url_prefix="/v1/csocial")


@csocial_bp.route('/cuenta-csocial',methods=['GET'])
@validar_rut(param_name='rut-titular')
@parse_query_params(
    rut_titular=int
)
def obtener_csocial(rut_titular):
    q=f"?rut-titular={rut_titular}"
    return forward_request('csocial',f"v1/cuenta-csocial{q}")

@csocial_bp.route('/cuenta-csocial/ultimos-movimientos',methods=['GET'])
@parse_query_params(
    nro_cuenta=int
)
def obtener_mov_csocial(nro_cuenta):
    numero_cuenta=f"?numero-cuenta={nro_cuenta}"
    return forward_request('csocial',f"v1/cuenta-csocial/ultimos-movimientos{numero_cuenta}")



