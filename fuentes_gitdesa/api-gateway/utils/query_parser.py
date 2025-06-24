from flask import request, jsonify
from functools import wraps
from typing import Dict, Any

def parse_query_params(convert_underscore=True,**param_specs):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            parsed = {}

            if convert_underscore:
                param_map = {name: name.replace('_', '-') for name in param_specs.keys()}
            else:
                param_map = {name: name for name in param_specs.keys()}
            
            for py_name, spec in param_specs.items():
                url_name = param_map[py_name]
                if isinstance(spec, type):
                    ptype = spec
                    default = ...
                else:
                    ptype, default = spec

                value = request.args.get(url_name)
                if value is None:
                    if default is ...:
                        return jsonify({"error": f"Parámetro requerido: {url_name}"}), 400
                    parsed[py_name] = default
                else:
                    try:
                        parsed[py_name] = ptype(value)
                    except (ValueError, TypeError):
                        return jsonify({
                            "error": f"Valor inválido para '{url_name}'. Debe ser de tipo {ptype.__name__}"
                        }), 400
            kwargs.update(parsed)
            return f(*args, **kwargs)
        return wrapped
    return decorator
