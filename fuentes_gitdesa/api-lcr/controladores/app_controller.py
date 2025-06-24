from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class LcrController(BaseController):
    """
    Controlador para manejar solicitudes relacionadas con las lcr
    """

    def __init__(self):
        super()

    @handle_exceptions
    def obtener_lineacr(self):
        """
        Maneja las solicitude GET para obtener informaicion de la linea cc por rut
        """
        rut = request.args.get('rut',type=int)
        response ,status_code= servicios.get_lineacr(rut)
        response,status_code = self._format_response(response,status_code)
        return jsonify(response),status_code

    @handle_exceptions
    def obtener_mov_lineacr(self):
        """
        Maneja las solicitude GET para obtener movimientos de la lineacr por numero de cuenta
        """
        nro_cuenta = request.args.get('nro_cuenta',type=int)
        cantidad = request.args.get('cantidad', default = 5, type=int)
        response ,status_code= servicios.get_mov_lineacr(nro_cuenta, cantidad)
        response,status_code = self._format_response(response,status_code)
        return jsonify(response),status_code

