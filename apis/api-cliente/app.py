import funciones_db
from servicios import servicios 
from utils.jwt_utils import JWTManager
from flask import Flask, request, jsonify, Blueprint
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

@app_v1.route('/auth/login', methods=['POST'])
def login_controller():
    try:
        data = request.get_json()
        rut = data.get("rut")
        clave = data.get("clave")

        if not rut or not clave:
            return jsonify({"error": "Rut y Clave son requeridos"}), 400

        response, status_code = servicios.login(rut, clave)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error en el inicio de sesión: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/obtener-cliente', methods=['GET'])
def get_usuario_por_rut_controller():
    try:
        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_usuario_por_rut(rut)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener usuario por RUT: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500


@app_v1.route('/direccion', methods=['GET'])
def obtener_direccion_cliente_controller():
    try:
        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_direccion_cliente(rut)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener dirección del cliente: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app_v1.route('/telefono', methods=['GET'])
def obtener_telefono_cliente_controller():
    try:

        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_telefono_cliente(rut)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener teléfono del cliente: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500


@app_v1.route('/telefono-verificado', methods=['GET'])
def obtener_telefono_verificado_cliente_controller():
    try:

        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_telefono_verificado_cliente(rut)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener teléfono verificado del cliente: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500


@app_v1.route('/obtener-correo', methods=['GET'])
def obtener_correo_cliente_controller():
    try:

        rut = request.args.get('rut',type=int)
        response, status_code = servicios.get_correo_cliente(rut)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener correo del cliente: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500


@app_v1.route('/funcionarios/sucursal', methods=['GET'])
def obtener_sucursal_funcionario_controller():
    try:
        usuario= request.args.get('usuario',type=int)
        response, status_code = servicios.get_sucursal_funcionario(usuario)
        return jsonify(response), status_code

    except Exception as e:
        logger.error(f"Error al obtener sucursal del funcionario: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500


app.register_blueprint(app_v1)



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])








