#from funciones_db import create_session_pool,pkg_exe_par_cursor,pkg_exe_error_msg_cursor
import funciones_db
from flask import Flask, request, jsonify, Blueprint
from servicios import servicios
import yaml
import cx_Oracle
from cx_Oracle import SessionPool
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




#################################################
# Cargar la configuración desde el archivo YAML #
#################################################
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)


app_config = config['app']
app_v1 = Blueprint('api_v1',__name__,url_prefix='/v1')

###############################################
#####    Manejador de errores 404    ##########
###############################################
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso no encontrado", "message": "La URL solicitada no existe"}), 404


@app_v1.route('/sucursales/activas', methods=['GET'])
def get_sucursales_activas():
    try:
        response, status_code = servicios.get_sucursales_activas()
        return jsonify(response), status_code
    except Exception as e:
        logger.error(f"Error al obtener sucursales activas: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/sucursal', methods=['GET'])
def get_sucursal_por_codigo():
    try:
        codigo = request.args.get('codigo',type=int)
        response, status_code = servicios.get_sucursal_por_codigo(codigo)
        return jsonify(response), status_code
    except Exception as e:
        logger.error(f"Error al obtener información de sucursal: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/comunas', methods=['GET'])
def get_comunas():
    try:
        comuna = request.args.get('comuna',default=-1,type=int)
        ciudad = request.args.get('ciudad',default=-1,type=int)
        response, status_code = servicios.get_comunas(comuna, ciudad)
        return jsonify(response), status_code
    except Exception as e:
        logger.error(f"Error al obtener información de comunas: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/ciudades', methods=['GET'])
def get_ciudades():
    try:
        ciudad = request.args.get('ciudad',type=int)
        response, status_code = servicios.get_ciudades(ciudad)
        return jsonify(response), status_code
    except Exception as e:
        logger.error(f"Error al obtener información de ciudades: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/parametros-sgt', methods=['GET'])
def get_parametros_sgt():
    try:
        response, status_code = servicios.get_parametros_sgt()
        return jsonify(response), status_code
    except Exception as e:
        logger.error(f"Error al obtener información de parámetros SGT: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

app.register_blueprint(app_v1)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])

