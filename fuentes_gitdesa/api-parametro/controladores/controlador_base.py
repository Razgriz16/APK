from flask import jsonify, g
from utils.respuesta_util import estandarizar_respuesta

class BaseController:
    """
    Clase base para controladores.
    """
    def __init__(self):
        """
        Inicializa el controlador con las funciones de base de datos.
        """

    def _format_response(self, response, status_code):
        """
        Formatea la respuesta para asegurar consistencia.
        """
        response, status_code = estandarizar_respuesta(response, status_code)
        if not isinstance(response, dict):
            g.logger.error(f"Formato de respuesta inesperado: {response}")
            return {
                "error_code": 500,
                "error_message": "Error en formato de respuesta del servicio",
                "trace_id": g.trace_id,
                "data": []
            }, 500
        if "trace_id" not in response:
            response["trace_id"] = g.trace_id
        return response, status_code

    def _create_error_response(self, error_code, error_message, status_code):
        """
        Crea una respuesta de error estándar.
        """
        return {
            "error_code": error_code,
            "error_message": error_message,
            "trace_id": g.trace_id,
            "data": []
        }, status_code
