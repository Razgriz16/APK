from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class LccController(BaseController):
    """
    Controlador para manejar solicitudes relacionadas con las lcc
    """

    def __init__(self):
        super()

    @handle_exceptions
    def obtener_lineacc(self):
        """
        Maneja las solicitude GET para obtener informaicion de la linea cc por rut
        """
        rut = request.args.get('rut',type=int)
        response ,status_code= servicios.get_lineacc(rut)
        response,status_code = self._format_response(response,status_code)
        return jsonify(response),status_code

