from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class CuentaAhorroController(BaseController):

    def __init__(self):
        super()

    @handle_exceptions
    def health(self):
        return jsonify("OK"),200

    @handle_exceptions
    def obtener_cliente(self):
        rut_titular = request.args.get('rut-titular',type=int)
        codigo_producto= request.args.get('codigo-producto',default=0,type=int)
        response, status_code = servicios.obtener_cuenta_ahorro(rut_titular,codigo_producto)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_movimientos(self):
        codigo_cuenta = request.args.get('numero-cuenta',type=int)
        fecha_inicio = request.args.get('fecha-inicio',default='0',type=str)
        fecha_fin = request.args.get('fecha-fin',default='0',type=str)
        response, status_code = servicios.obtener_movimientos(codigo_cuenta,fecha_inicio,fecha_fin)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def verificar_bloqueo_dbf_uaf(self):
        rut = request.args.get('rut',type=int)
        response, status_code = servicios.verificar_existencia_bloqueo(rut)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_ultimos_movimientos(self):
        codigo_cuenta = request.args.get('numero-cuenta',type=int)
        cantidad = request.args.get('cantidad',default=5,type=int)
        response, status_code = servicios.obtener_ultimos_movimientos(codigo_cuenta,cantidad)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code
