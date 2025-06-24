from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request

lcc_bp = Blueprint("lcc",__name__, url_prefix="/v1/lcc")


@lcc_bp.route('/lineacc',methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_lineacc(rut):
    q=f"?rut={rut}"
    return forward_request('lineacc',f"v1/lineacc{q}")

@lcc_bp.route('/lineacc/movimientos',methods=['GET'])
@parse_query_params(
    nro_cuenta=int,
    cantidad = (5,int)
)
def obtener_mov_lineacc(nro_cuenta, cantidad):
    numero_cuenta=f"?numero-cuenta={nro_cuenta}&cantidad={cantidad}"
    return forward_request('lineacc',f"v1/lineacc/movimientos{numero_cuenta}")


@lcc_bp.route('/lineacc/facturas',methods=['GET'])
@parse_query_params(
    nro_cuenta=int
)
def obtener_fac_lineacc(nro_cuenta):
    numero_cuenta=f"?numero-cuenta={nro_cuenta}"
    return forward_request('lineacc',f"v1/lineacc/facturas{numero_cuenta}")




