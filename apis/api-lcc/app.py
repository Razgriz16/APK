#from funciones_db import create_session_pool,pkg_exe_par_cursor,pkg_exe_error_msg_cursor
import funciones_db
from flask import Flask, request, jsonify
import yaml
import cx_Oracle
from cx_Oracle import SessionPool


app = Flask(__name__)


#################################################
# Cargar la configuración desde el archivo YAML #
#################################################
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)


app_config = config['app']

###############################################
#####    Manejador de errores 404    ##########
###############################################
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso no encontrado", "message": "La URL solicitada no existe"}), 404


#############################################
######    Recuperar un cliente      #########
#############################################
@app.route('/obtener_cliente', methods=['GET'])
def obtener_cliente():
    rut = request.args.get('rut')
    if not rut:
        return jsonify({"error": "Faltan parámetros"}), 400

    package_name = "CLIENTE.PCK_CLIENTE"  # Reemplaza con el nombre de tu package
    procedure_name = "CliRecCliente"  # Reemplaza con el nombre de tu procedimiento

    # Parámetros para el procedimiento (en este caso, solo el RUT)
    params = [rut]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###########################################
#### Recuperar Direcciones x rut  #########
###########################################
@app.route('/obtener_direcciones', methods=['GET'])
def obtener_comunas():
    rut = request.args.get('rut')

    package_name = "CLIENTE.PCK_CLIENTE"  # Reemplaza con el nombre de tu package
    procedure_name = "CLIRECDIRECCION"  # Reemplaza con el nombre de tu procedimiento

    # Parámetros para el procedimiento (en este caso, solo el RUT)
    params = [rut]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###########################################
##### Recuperar telefonos x rut   #########
###########################################
@app.route('/obtener_telefonos', methods=['GET'])
def obtener_ciudades():
    rut = request.args.get('rut')

    package_name = "CLIENTE.PCK_CLIENTE"  # Reemplaza con el nombre de tu package
    procedure_name = "CLIRECTELEFONO"  # Reemplaza con el nombre de tu procedimiento

    # Parámetros para el procedimiento (en este caso, solo el RUT)
    params = [rut]

    # Ejecutar el procedimiento y obtener la respuesta
    response, status_code = funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])
