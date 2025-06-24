from flask import g
import traceback

def handle_service_error(error, context=""):
    """
    Maneja errores en servicios y genera una respuesta estándar.
    
    Args:
        error (Exception): Excepción capturada.
        context (str): Contexto del error para el logging.
        
    Returns:
        tuple: (response_dict, status_code) con la respuesta de error.
    """
    g.logger.error(f"{context}: {str(error)}")
    g.logger.error(traceback.format_exc())
    
    return {
        "error_code": 500,
        "error_message": "Error al procesar la solicitud",
        "trace_id": g.trace_id,
        "data": []
    }, 500
