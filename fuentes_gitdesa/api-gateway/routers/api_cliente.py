from flask import Flask, Blueprint, current_app, request,jsonify, make_response
from middlewares.validar_rut import validar_rut
from utils.query_parser import parse_query_params
from utils.forward_request import forward_request
import json

cliente_bp = Blueprint("cliente",__name__, url_prefix="/v1/cliente")



@cliente_bp.route('/auth/login', methods=['POST'])
def login():
    response_data,status_code,_ =  forward_request('cliente','v1/auth/login')
    if status_code != 200:
        return jsonify(response_data),status_code

    current_app.logger.info(response_data)
    if isinstance(response_data, bytes):
        try:
            response_data = json.loads(response_data.decode('utf-8'))
        except json.JSONDecodeError:
            return jsonify({"error": "Respuesta no es JSON válido"}), 500

    if isinstance(response_data, dict):
        data_list = response_data.get("data")
        if data_list and isinstance(data_list, list) and len(data_list) > 0:
            user_data = data_list[0]
            access_token = user_data.get("access_token")
            refresh_token = user_data.get("refresh_token")
        else:
            return jsonify({"error": "Datos de usuario no encontrados"}), 500
    else:
        return jsonify({"error": "Formato de respuesta inválido"}), 500

    if not isinstance(refresh_token, str):
        return jsonify({"error": "Refresh token inválido o ausente"}), 500

    response_body = {"access_token":access_token}
    response =  make_response(jsonify(response_body),status_code)

    response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite='Lax',
        max_age= 60 * 15,
        path='/auth/refrescar-token'
    )

    return response

@cliente_bp.route('/cliente', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_usuario_por_rut(rut):
    q =f"?rut={rut}"
    return forward_request('cliente',f"v1/cliente{q}")


@cliente_bp.route('/cliente/direccion', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_direccion_cliente(rut):
    q =f"?rut={rut}"
    return forward_request('cliente',f"v1/cliente/direccion{q}")



@cliente_bp.route('/cliente/telefono', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_telefono_cliente(rut):
    q = f"?rut={rut}"
    return forward_request('cliente',f"v1/cliente/telefono{q}")


@cliente_bp.route('/cliente/telefono-verificado', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_telefono_verificado_cliente(rut):
    q = f"?rut={rut}"
    return forward_request('cliente',f"v1/cliente/telefono-verificado{q}")



@cliente_bp.route('/cliente/correo', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_correo_cliente(rut):
    q = f"?rut={rut}"
    return forward_request('cliente',f"v1/cliente/correo{q}")


@cliente_bp.route('/funcionario/sucursal', methods=['GET'])
@validar_rut(param_name='rut')
@parse_query_params(
    rut=int
)
def obtener_sucursal_funcionario(rut):
    q = f"?rut={rut}"
    return forward_request('cliente', f"v1/funcionario/sucursal{q}")

@cliente_bp.route('/auth/refrescar-token',methods=['POST'])
def refrescar_token():
    refresh_token = request.cookies.get('refresh_token')
    if not refresh_token:
        return jsonify({"error":"Refresh token no encontrado"}),401
    return forward_request(service='cliente',path='v1/auth/refrescar-token',json={'token':refresh_token})
