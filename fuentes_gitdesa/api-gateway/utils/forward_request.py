import requests 
from  flask import jsonify,current_app, request
import yaml

# Cargar la configuración desde el archivo YAML
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

service_mapping = config['service_mapping']



def forward_request(service, path, json=None):
    """
    Funcion para realizar las consultas a los diferentes endpoints de cada microservicios
    """

    try:
        service_url = service_mapping.get(service)
        if not service_url:
            return jsonify({"error": "Microservicio no encontrado"}), 404

        current_app.logger.info(service_url)

        full_url = f"{service_url}/{path}"
        current_app.logger.info(full_url)

        response = requests.request(
            method=request.method,
            url=full_url,
            headers={key: value for key, value in request.headers if key != 'Host'},
            json=json if json is not None else request.get_json(silent=True),
            data=None if json is not None else request.get_data(),
            params=request.args,
            timeout=5  # Timeout para evitar bloqueos
        )

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = {key: value for key, value in response.headers.items() if key.lower() not in excluded_headers}

        current_app.logger.info(response.content)
        return response.content, response.status_code, headers
    except requests.exceptions.Timeout:
        return jsonify({"error": "Timeout al conectar con el microservicio"}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "No se pudo conectar con el microservicio"}), 503
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500
