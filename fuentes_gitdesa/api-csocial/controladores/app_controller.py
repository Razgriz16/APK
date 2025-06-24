from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class CsocialController(BaseController):

    def __init__(self):
        super()

    @handle_exceptions
    def health(self):
        return jsonify("OK"),200

    @handle_exceptions
    def obtener_cliente(self):
        rut_titular = request.args.get('rut-titular',type=int)
        response, status_code = servicios.obtener_cuenta_csocial(rut_titular)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

#    @handle_exceptions
#    def verificar_bloqueo_dbf_uaf(self):
#        rut = request.args.get('rut',type=int)
#        response, status_code = servicios.verificar_existencia_bloqueo(rut)
#        response, status_code = self._format_response(response,status_code)
#        return jsonify(response), status_code

    @handle_exceptions
    def obtener_ultimos_movimientos(self):
        cuenta = request.args.get('numero-cuenta',type=int)
        cantidad = request.args.get('cantidad',default=5,type=int)
        response, status_code = servicios.obtener_ultimos_movimientos(cuenta,cantidad)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code
