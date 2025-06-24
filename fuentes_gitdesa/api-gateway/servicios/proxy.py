import requests
from flask import jsonify
from config import config 

class ServiceProxy:
    @staticmethod
    def forward_request(service_name, path, method, headers, data=None, params=None):
        service_url = config['service_mapping'].get(service_name)
        if not service_url:
            return jsonify({"error": "Microservicio no encontrado"}), 404
        full_url = f"{service_url}/{path}"
        try:
            response = requests.request(
                method=method,
                url=full_url,
                headers=headers,
                data=data,
                params=params,
                timeout=5
            )
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            filtered_headers = {key: value for key, value in response.headers.items() if key.lower() not in excluded_headers}

            return response.content, response.status_code, filtered_headers
        except requests.exceptions.Timeout:
            return jsonify({"error": "Se acabo el timepo de esperar para conectar con el microservicio"}), 504
        except requests.exceptions.ConnectionError:
            return jsonify({"error": "Error al intentar conectar con el microservicio"}), 503
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
