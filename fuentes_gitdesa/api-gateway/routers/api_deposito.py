from flask import Flask, Blueprint, current_app
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request

deposito_bp = Blueprint("deposito",__name__, url_prefix="/v1/deposito")


@deposito_bp.route('/recuperar-dap',methods=['GET'])
@validar_rut(param_name='rut_cliente')
@parse_query_params(
    rut=int,
    estado=int,
    fecha_inicio=str,
    fecha_fin=str,
    indicador1=str,
    indicador2=str
)
def obtener_dap(rut, estado, fecha_inicio, fecha_fin, indicador1, indicador2):
    q=f"?rut_cliente={rut}&estado={estado}&fecha_inicio={fecha_inicio}&fecha_fin={fecha_fin}&indicador1={indicador1}&indicador2={indicador2}"
    return forward_request('deposito',f"v1/recuperar-dap{q}")

