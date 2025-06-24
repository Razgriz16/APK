from flask import g
from .error_adapter import OracleErrorAdapter

def validar_respuesta_oracle(error_code=None, error_message=None, data=None, context=""):
    """
    Valida la respuesta de un procedimiento Oracle
    Retorna (respuesta_error, código_http) si hay error, o (None, None) si no hay error
    """
    if error_code is None or error_code == 0:
        return None, None

    mensaje, http_code = OracleErrorAdapter.translate(error_code, error_message)
    g.logger.warning(f"{context}: {mensaje} (Código: {error_code})")

    response = {
        "error_code": error_code,
        "error_message": mensaje,
        "trace_id": g.trace_id,
        "data": data or []
    }

    return response, http_code
