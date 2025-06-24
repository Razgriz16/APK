from flask import Flask, g,jsonify
import logging
import uuid
from rutas.rutas import app_v1
import yaml


def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)
    app.logger = logging.getLogger(__name__)

    #################################################
    # Cargar la configuración desde el archivo YAML #
    #################################################
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        app_config=config['app']

    app.config.update(app_config)

    @app.before_request
    def before_request():
        g.logger = app.logger
        g.trace_id = str(uuid.uuid4())



    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error":"Recurso no encontrado","message":"La URL solicitada no existe"}),404


    app.register_blueprint(app_v1,url_prefix='/v1')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port= app.config['port'], debug=app.config['debug'])
