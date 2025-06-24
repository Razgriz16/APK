import re
class OracleErrorAdapter:
    ERROR_MAPPING = {
        -1: {"message": "Registro no encontrado", "http_code": 404},
        -100: {"message": "Parámetro inválido", "http_code": 400},
        -1403: {"message": "No se encontraron datos", "http_code": 404},
        -6550: {"message": "Error de sintaxis en la consulta PL/SQL", "http_code": 500},
        -201: {"message": "El identificador debe declararse", "http_code": 500},
    }

    ORA_PATTERNS = {
        r"ORA-06550.*PLS-00201.*se\s+debe\s+declarar": {
            "message": "El procedimiento o función especificado no existe en la base de datos",
            "http_code": 500
        },
        r"ORA-06550": {
            "message": "Error de sintaxis en la consulta PL/SQL",
            "http_code": 500
        },
    }

    @staticmethod
    def translate(error_code, error_message):
        if error_code == 0:
            return None, None

        # Para errores ORA en el mensaje, buscamos patrones específicos
        if error_message and isinstance(error_message, str) and "ORA-" in error_message:
            for pattern, info in OracleErrorAdapter.ORA_PATTERNS.items():
                if re.search(pattern, error_message, re.IGNORECASE):
                    return info["message"], info["http_code"]

        if error_code is None:
            return f"Error desconocido de base de datos, {error_message}",500

        # Buscamos el código de error en el mapping
        error_info = OracleErrorAdapter.ERROR_MAPPING.get(error_code, None)
        if error_info:
            return error_info["message"], error_info["http_code"]

        # Error por defecto
        return error_message or f"Error de base de datos ({error_code})", 500 if error_code < -200 else 400


