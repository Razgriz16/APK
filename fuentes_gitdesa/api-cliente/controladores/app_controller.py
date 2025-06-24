from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios

class ClientesController(BaseController):
    """
    Controlador para manejar solicitudes relacionadas con clientes
    """

    def __init__(self):
        super();

    @handle_exceptions
    def login(self):
        """
        Maneja la solicitud POST para iniciar sesión.
        """
        data = request.get_json()
        rut = data.get("rut")
        clave = data.get("clave")
        if not rut or not clave:
            g.logger.warning("Parámetros 'rut' o 'clave' no proporcionados")
            return jsonify(self._create_error_response(
                400, "Rut y Clave son requeridos", 400
            ))
        response, status_code = servicios.login(rut, clave)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_usuario_por_rut(self):
        """
        Maneja la solicitud GET para obtener información de un usuario por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        response, status_code = servicios.get_usuario_por_rut(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_direccion_cliente(self):
        """
        Maneja la solicitud GET para obtener la dirección de un cliente por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        response, status_code = servicios.get_direccion_cliente(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_telefono_cliente(self):
        """
        Maneja la solicitud GET para obtener el teléfono de un cliente por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        response, status_code = servicios.get_telefono_cliente(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_telefono_verificado_cliente(self):
        """
        Maneja la solicitud GET para obtener el teléfono verificado de un cliente por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        g.logger.info(f"Consulta de teléfono verificado de cliente. RUT: {rut}")
        response, status_code = servicios.get_telefono_verificado_cliente(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_correo_cliente(self):
        """
        Maneja la solicitud GET para obtener el correo de un cliente por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        response, status_code = servicios.get_correo_cliente(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_sucursal_funcionario(self):
        """
        Maneja la solicitud GET para obtener la sucursal de un funcionario por RUT.
        """
        rut = request.args.get('rut', type=int)
        if rut is None:
            g.logger.warning("Parámetro 'rut' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'rut' es obligatorio", 400
            ))
        response, status_code = servicios.get_sucursal_funcionario(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code
