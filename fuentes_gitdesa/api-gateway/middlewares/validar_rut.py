from flask import request, jsonify, current_app
from functools import wraps



def validar_rut(param_name=None, in_path=False):
    def decorador(f):
        @wraps(f)
        def fn_decorada(*args,**kwargs):
            if not hasattr(request,'user') or 'rut_usuario' not in request.user:
                return jsonify({"error":"Cliente no autenticado"}),401

            user_rut = str(request.user['rut_usuario'])
            request_rut = None
            current_app.logger.info(user_rut)

            if in_path and param_name in kwargs:
               request_rut = kwargs[param_name]
            elif param_name:
                if param_name in request.args:
                    request_rut = request.args.get(param_name)
                elif request.is_json and param_name in request.json:
                    request_rut = request.json.get(param_name)
                elif param_name in request.form:
                    request_rut = request.form.get(param_name)
            current_app.logger.info(f"User RUT: {user_rut}, Request RUT: {request_rut}")
            if request_rut is not None and str(user_rut) != str(request_rut):
                current_app.logger.warning({"error":"Rut no autorizado. Cliente {user_rut} - Solicidatod {request_rut}"}),403
                return jsonify({"error":"Cliente no tiene autorizacion para acceder a los datos seleccionados"}),403
            return f(*args,**kwargs)
        return fn_decorada
    return decorador
