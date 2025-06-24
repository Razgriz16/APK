from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class DapController(BaseController):

    def __init__(self):
        super()

    @handle_exceptions
    def health(self):
        return jsonify("OK"),200

    @handle_exceptions
    def recuperar_operaciones(self):
        rut_cliente = request.args.get('rut_cliente',type=int)
        estado = request.args.get('estado', type=int)
        fecha_inicio = request.args.get('fecha_inicio', type=str)
        fecha_fin = request.args.get('fecha_fin', type=str)
        indicador1 = request.args.get('indicador1', type=str)
        indicador2 = request.args.get('indicador2', type=str)
        response, status_code = servicios.recuperar_operaciones(rut_cliente, estado, str(fecha_inicio), str(fecha_fin), indicador1, indicador2)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code
