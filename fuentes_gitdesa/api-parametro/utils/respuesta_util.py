from datetime import datetime
from flask import g, current_app
from .validacion_util import validar_respuesta_oracle
from .error_util import handle_service_error
import re

def estandarizar_respuesta(response, status_code):
    """
    Estandariza la respuesta de un procedimiento PL/SQL.
    
    Args:
        response: Respuesta cruda del procedimiento (puede ser dict, list, etc.).
        status_code (int): Código de estado retornado por el procedimiento.
        
    Returns:
        tuple: (response_dict, status_code) donde response_dict es un diccionario
              con error_code, error_message, y data.
    """
    if isinstance(response, list) or not isinstance(response, dict):
        return {
            "error_code": 0,
            "error_message": "",
            "data": response
        }, 200
    return response, status_code

def respuesta_completa(data):
    """
    Respuesta exitosa con campos estándar.
    
    Args:
        data: Lista o datos a incluir en la respuesta.
        
    Returns:
        dict: Respuesta con error_code, error_message, trace_id,
              timestamp, count, y data.
    """
    return {
        "error_code": 0,
        "error_message": "",
        "trace_id": g.trace_id,
        "count": len(data) if isinstance(data, list) else 0,
        "data": data
    }

def procesar_respuesta_plsql(response, status_code, context=""):
    """
    Procesa una respuesta de un procedure de funciones_db.py
    
    Args:
        response: Respuesta del procedimiento.
        status_code (int): codigo de estado retornado por el procedimiento.
        context (str): Contexto para logging.
        
    Returns:
        tuple: (response_dict, status_code) con la respuesta procesada o un error.
    """
    try:

        if isinstance(response,dict) and 'error' in response:
            error_msg = response['error']
            ora_match = re.search(r'ORA-(\d+)', error_msg)
            error_num = -int(ora_match.group(1)) if ora_match else -6550

            error_response, http_code = validar_respuesta_oracle(
                error_code=error_num,
                error_message=error_msg,
                context=context
            )
            return error_response,http_code

        # Estandarizamos la respuesta
        response, status_code = estandarizar_respuesta(response, status_code)


        # Validamos la estructura básica de la respuesta
        if not isinstance(response, dict):
            g.logger.error(f"Respuesta con formato inválido: {response}")
            return {
                "error_code": 500,
                "error_message": "Error en formato de respuesta del procedimiento",
                "trace_id": g.trace_id,
                "data": []
            }, 500

        # Extraemos error_code y error_message si existen
        error_code = response.get("error_code", None)
        error_message = response.get("error_message", None)

        # Validamos la respuesta del PL/SQL
        error_response, http_code = validar_respuesta_oracle(
            error_code,
            error_message,
            context=context
        )

        if error_response:
            return error_response, http_code

        # Procesamos los datos y enriquecemos la respuesta
        data = response.get("data", [])
        enriched_response = respuesta_completa(data)

        g.logger.info(f"Procedimiento ejecutado correctamente. Registros: {enriched_response['count']}")
        return enriched_response, 200

    except Exception as e:
        return handle_service_error(e, context=context)
