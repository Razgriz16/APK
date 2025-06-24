from flask import Flask, request, jsonify, current_app
import requests
import yaml
from middlewares.auth_middleware import auth_jwt
from middlewares.validar_rut import validar_rut 
from utils.forward_request import forward_request
from routers.api_credito import creditos_prorroga_bp

app = Flask(__name__)

# Cargar la configuración desde el archivo YAML
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

service_mapping = config['service_mapping']
app_config = config['gateway']

@app.before_request
@auth_jwt
def before_request():
    current_app.logger.info(f"Request autenticada: {request.method} {request.path}")


@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    try:
        # Obtener la URL del microservicio
        service_url = service_mapping.get(service)
        if not service_url:
            return jsonify({"error": "Microservicio no encontrado"}), 404
       
        # Construir la URL completa
        full_url = f"{service_url}/{path}"

        # Forward de la solicitud al microservicio
        response = requests.request(
            method=request.method,
            url=full_url,
            headers={key: value for key, value in request.headers if key != 'Host'},
            data=request.get_data(),
            params=request.args,
            timeout=5  # Timeout para evitar bloqueos
        )

        # Devolver la respuesta del microservicio
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = {key: value for key, value in response.headers.items() if key.lower() not in excluded_headers}

        return response.content, response.status_code, headers

    except requests.exceptions.Timeout:
        return jsonify({"error": "Timeout al conectar con el microservicio"}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "No se pudo conectar con el microservicio"}), 503
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_config['port'],debug=app_config['debug'])

