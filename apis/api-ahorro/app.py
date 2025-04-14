#from funciones_db import create_session_pool,pkg_exe_par_cursor,pkg_exe_error_msg_cursor
import funciones_db
from servicios import servicios
from flask import Flask, request, jsonify, current_app
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
######    Recuperar cuenta ahorro   #########
#############################################
@app.route('/obtener_cuenta_ahorro', methods=['GET'])
def obtener_cliente():
    
    #Params necesarios
    rut_titular = request.args.get('rut-titular',type=int)
    codigo_producto= request.args.get('codigo-producto',type=int)


    # Ejecutar el servicio
    response, status_code = servicios.obtener_cuenta_ahorro(rut_titular,codigo_producto)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###################################################
######    Recuperar movimientos de cuenta  ########
###################################################
@app.route('/obtener_movimientos', methods=['GET'])
def obtener_movimientos():
    
    #Params necesarios
    codigo_cuenta = request.args.get('numero_cuenta',type=int)
    fecha_inicio = request.args.get('fecha_inicio',default='0',type=str)
    fecha_fin = request.args.get('fecha_fin',default='0',type=str)

    # Ejecutar el servicio
    response, status_code = servicios.obtener_movimientos(codigo_cuenta,fecha_inicio,fecha_fin)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


#################################################################
######    Verificar la existencia de un bloqueo DBF UAF  ########
#################################################################
@app.route('/v1/cuentas-ahorro/cuenta/bloqueo-dbuaf',methods=['GET'])
def verificar_bloqueo_dbf_uaf():
    #Params necesarios
    rut = request.args.get('rut',type=int)

    # Ejecutar el servicio
    response, status_code = servicios.verificar_existencia_bloqueo(rut)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code




if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])
