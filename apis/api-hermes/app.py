
from servicios import servicios
from  flask import Flask, request, jsonify, current_app
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
######    Recuperar  Usuario        #########
#############################################
@app.route('/obtener_usuario', methods=['GET'])
def obtener_usuario():
    """
    Endpoint para obtener usuario
    """
    #Params necesarios
    id = request.args.get('identificador',type=int)

    response, status_code = servicios.obtener_usuario(id)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


########################################################
######    Recuperar  Privilegios Del Usuario    ########
########################################################
@app.route('/obtener_privilegios_usuario', methods=['GET'])
def obtener_privilegios_usuario():
    """
    Endpoint para obtener privilegios del usuario 
    """
    #Params necesarios
    id = request.args.get('identificador',type=int)
    sistema  = request.args.get('sistema',type=int)

    response, status_code = servicios.obtener_privilegios_usuario(id,sistema)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###################################################
######    Recuperar Usuarios Por Accion    ########
###################################################
@app.route('/obtener_usuarios_accion', methods=['GET'])
def obtener_usuarios_accion():
    """
    Endpoint para obtener privilegios del usuario 
    """
    #Params necesarios
    accion = request.args.get('accion',type=int)
    sistema  = request.args.get('sistema',type=int)

    response, status_code = servicios.obtener_usuario_accion(accion,sistema)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###################################
######    Valida accion    ########
###################################
@app.route('/valida-accion', methods=['GET'])
def obtener_valida_accion():
    """
    Endpoint para obtener acciones del usuario
    """
    #Params necesarios
    idusuario = request.args.get('idusuario',type=int)
    accion  = request.args.get('accion',type=int)

    response, status_code = servicios.obtener_acciones_usuario(idusuario,accion)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code




if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])

