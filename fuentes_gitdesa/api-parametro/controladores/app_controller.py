from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios

class ParametrosController(BaseController):
    """
    Controlador para manejar solicitudes relacionadas con parámetros generales.
    """

    def __init__(self):
        super()

    @handle_exceptions
    def obtener_sucursales_activas(self):
        """
        Maneja la solicitud GET para obtener las sucursales activas.
        """
        g.logger.info("Consulta de sucursales activas")
        response, status_code = servicios.get_sucursales_activas()
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_sucursal_por_codigo(self):
        """
        Maneja la solicitud GET para obtener información de una sucursal por código.
        """
        codigo = request.args.get('codigo', type=int)
        if codigo is None:
            g.logger.warning("Parámetro 'codigo' no proporcionado")
            return jsonify(self._create_error_response(
                400, "El parámetro 'codigo' es obligatorio", 400
            ))
        g.logger.info(f"Consulta de información de sucursal. Código: {codigo}")
        response, status_code = servicios.get_sucursal_por_codigo(codigo)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_comunas(self):
        """
        Maneja la solicitud GET para obtener información de comunas.
        """
        comuna = request.args.get('comuna', default=-1, type=int)
        ciudad = request.args.get('ciudad', default=-1, type=int)
        
        g.logger.info(f"Consulta de comunas. Comuna: {comuna}, Ciudad: {ciudad}")
        response, status_code = servicios.get_comunas(comuna, ciudad)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_ciudades(self):
        """
        Maneja la solicitud GET para obtener información de ciudades.
        """
        ciudad = request.args.get('ciudad', default=-1, type=int)
        
        g.logger.info(f"Consulta de ciudades. Ciudad: {ciudad}")
        response, status_code = servicios.get_ciudades(ciudad)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_parametros_sgt(self):
        """
        Maneja la solicitud GET para obtener parámetros SGT.
        """
        g.logger.info("Consulta de parámetros SGT")
        response, status_code = servicios.get_parametros_sgt()
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_credito_bloqueado_test(self):
        """
        Maneja la solicitud GET para obtener parámetros SGT.
        """
        g.logger.info("Consulta de parámetros SGT")

        operacion = request.args.get('operacion', default=None, type=int)
        estado = request.args.get('estado', default='0', type=str)
        judicial = request.args.get('judicial', default='0', type=str)

        response, status_code = servicios.get_credito_bloqueo(operacion,estado,judicial)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def obtener_cliente_test(self):
        """
        Maneja la solicitud GET para obtener parámetros SGT.
        """
        g.logger.info("Consulta de parámetros SGT")
        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_cliente(rut)
        response, status_code = self._format_response(response, status_code)
        return jsonify(response), status_code






