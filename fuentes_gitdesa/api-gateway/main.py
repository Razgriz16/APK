from flask import Flask, request, jsonify, current_app
import requests
import yaml
from routers import register_blueprints
from middlewares.auth_middleware import auth_jwt

def create_app():
    app = Flask(__name__)

    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    app.config['service_mapping'] = config['service_mapping']
    app.config['gateway_config'] = config['gateway']

    @app.before_request
    @auth_jwt
    def before_request():
        current_app.logger.info(f"Request autenticada: {request.method} {request.path}")

    register_blueprints(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=app.config['gateway_config']['port'], debug=app.config['gateway_config']['debug'])
