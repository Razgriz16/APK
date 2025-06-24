import traceback
from functools import wraps
from flask import jsonify, g, current_app

def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            return jsonify({
                "error_code": 400,
                "error_message": str(e),
                "trace_id": g.trace_id,
                "data": None
            }), 400
        except Exception as e:
            g.logger.error(traceback.format_exc())
            error_message = f"Error interno del servidor. ID de referencia: {g.trace_id}"
            if current_app.config.get('DEBUG', False):
                error_message = f"Error interno: {str(e)}"
            return jsonify({
                "error_code": 500,
                "error_message": error_message,
                "trace_id": g.trace_id,
                "data": None
            }), 500
    return decorated_function
