#from funciones_db import create_session_pool,pkg_exe_par_cursor,pkg_exe_error_msg_cursor import funciones_db
from  servicios import servicios 
from flask import Flask, request, jsonify, current_app, Blueprint
import yaml
import cx_Oracle
from cx_Oracle import SessionPool
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

################################################# # Cargar la configuración desde el archivo YAML #
#################################################
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)


app_config = config['app']
app_v1 = Blueprint('api_v1', __name__, url_prefix='/v1')


###############################################
#####    Manejador de errores 404    ##########
###############################################
@app.errorhandler(404) 
def not_found_error(error):
   return jsonify({"error": "Recurso no encontrado", "message": "La URL solicitada no existe"}), 404


#################################
######     Health       #########
#################################
@app_v1.route('/health', methods=['GET'])
def health():
    # Devolver la respuesta en formato JSON
    return jsonify("OK"), 200




#############################################
######    Recuperar  Credito        #########
#############################################
@app_v1.route('/creditos', methods=['GET'])
def obtener_credito():
    """
    Endpoint para obtener creditos
    """
    #Params necesarios
    credito = request.args.get('credito',default=-1,type=int)
    estado = request.args.get('estado',default=-1,type=int)
    rut = request.args.get('rut',default=-1,type=int)
    prorrogados = request.args.get('prorrogados',default='N',type=str)

    response, status_code = servicios.get_credito(credito,rut,estado,prorrogados)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


#############################################
######    Bloqueo Credito         ###########
#############################################
@app_v1.route('/creditos/bloqueo', methods=['GET'])
def obtener_credito_bloqueo():
    """
    Endpoint para obtener bloqueos de crédito
    """
    operacion = request.args.get('operacion', default=None, type=int)
    estado = request.args.get('estado', default='0', type=str)
    judicial = request.args.get('judicial', default='0', type=str)
    response, status_code = servicios.get_credito_bloqueo(operacion, estado, judicial)
    return jsonify(response), status_code



#############################################
######    Cuotas                  ###########
#############################################
@app_v1.route('/creditos/cuotas', methods=['GET'])
def obtener_cuotas():
    """
    Endpoint para obtener cuotas de crédito
    """
    operacion = request.args.get('operacion', default=None, type=int)
    peso = request.args.get('peso', default='N', type=str)
    response, status_code = servicios.get_cuotas(operacion, peso)
    return jsonify(response), status_code

#############################################
######    Movimientos             ###########
#############################################
@app_v1.route('/creditos/movimientos', methods=['GET'])
def obtener_movimientos():
    """
    Endpoint para obtener movimientos de crédito
    """
    credito = request.args.get('credito', default=None, type=int)
    response, status_code = servicios.obtener_movimientos(credito)
    return jsonify(response), status_code

#############################################
######    Operaciones Cliente     ###########
#############################################
@app_v1.route('/operaciones/cliente', methods=['GET'])
def obtener_operaciones_cliente():
    """
    Endpoint para obtener operaciones de cliente
    """
    todos = request.args.get('todos', default=None, type=str)
    fecha = request.args.get('fecha', default=None, type=str)
    cliente = request.args.get('cliente', default=0, type=int)
    operacion = request.args.get('operacion', default=0, type=int)
    response, status_code = servicios.obtener_operaciones_cliente(todos, fecha, cliente, operacion)
    return jsonify(response), status_code

#############################################
######    Detalle Prorroga        ###########
#############################################
@app_v1.route('/prorrogas/detalle', methods=['GET'])
def obtener_detalle_prorroga():
    """
    Endpoint para obtener detalle de prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.obtener_detalle_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Rechazos Prorroga       ###########
#############################################
@app_v1.route('/prorrogas/rechazos', methods=['GET'])
def obtener_rechazos_prorroga():
    """
    Endpoint para obtener rechazos de prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_rechazos_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Cuotas Prorrogas        ###########
#############################################
@app_v1.route('/prorrogas/cuotas', methods=['GET'])
def obtener_cuotas_prorrogas():
    """
    Endpoint para obtener cuotas de prórrogas
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    cuota_desde = request.args.get('cuota_desde', default=None, type=int)
    cuota_hasta = request.args.get('cuota_hasta', default=None, type=int)
    response, status_code = servicios.get_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
    return jsonify(response), status_code

#############################################
######    Cuotas Prorrogas Posterior ########
#############################################
@app_v1.route('/prorrogas/cuotas/posterior', methods=['GET'])
def obtener_cuotas_prorrogas_posterior():
    """
    Endpoint para obtener cuotas posteriores de prórrogas
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_cuotas_prorrogas_posterior(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Detalle Cuotas Prorrogas Posterior #
#############################################
@app_v1.route('/prorrogas/cuotas/posterior/detalle', methods=['GET'])
def obtener_detalle_cuotas_prorrogas_posterior():
    """
    Endpoint para obtener detalle de cuotas posteriores de prórrogas
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_detalle_cuotas_prorrogas_posterior(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Cargos Prorroga         ###########
#############################################
@app_v1.route('/prorrogas/cargos', methods=['GET'])
def obtener_cargos_prorroga():
    """
    Endpoint para obtener cargos de prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_cargos_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Creditos Prorroga       ###########
#############################################
@app_v1.route('/prorrogas/creditos', methods=['GET'])
def obtener_creditos_prorroga():
    """
    Endpoint para obtener créditos de prórroga
    """
    rut = request.args.get('rut', default=None, type=int)
    response, status_code = servicios.get_creditos_prorroga(rut)
    return jsonify(response), status_code

#############################################
######    Rechazo Prorroga Usuario ##########
#############################################
@app_v1.route('/prorrogas/rechazos/usuario', methods=['GET'])
def obtener_rechazo_prorroga_usuario():
    """
    Endpoint para obtener rechazo de prórroga por usuario
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    id_usuario = request.args.get('id_usuario', default=None, type=int)
    response, status_code = servicios.get_rechazo_prorroga_usuario(id_prorroga, id_usuario)
    return jsonify(response), status_code

#############################################
######    Parametros              ###########
#############################################
@app_v1.route('/parametros', methods=['GET'])
def obtener_parametros():
    """
    Endpoint para obtener parámetros
    """
    response, status_code = servicios.get_parametros()
    return jsonify(response), status_code

#############################################
######    Grupo Prorrogas         ###########
#############################################
@app_v1.route('/prorrogas/grupo', methods=['GET'])
def obtener_grupo_prorrogas():
    """
    Endpoint para obtener grupo de prórrogas
    """
    codigo = request.args.get('codigo', default=None, type=int)
    response, status_code = servicios.get_grupo_prorrogas(codigo)
    return jsonify(response), status_code

#############################################
######    Detalle Cuota Posterior Prorroga ##
#############################################
@app_v1.route('/prorrogas/cuota/posterior/detalle', methods=['GET'])
def obtener_detalle_cuota_posterior_prorroga():
    """
    Endpoint para obtener detalle de cuotas posteriores de la prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_detalle_cuota_posterior_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Detalle Cuota Anterior Prorroga ###
#############################################
@app_v1.route('/prorrogas/cuota/anterior/detalle', methods=['GET'])
def obtener_detalle_cuota_anterior_prorroga():
    """
    Endpoint para obtener detalle de cuotas anteriores de la prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_detalle_cuota_anterior_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Detalle Cargos Prorroga ###########
#############################################
@app_v1.route('/prorrogas/cargos/detalle', methods=['GET'])
def obtener_detalle_cargos_prorroga():
    """
    Endpoint para obtener el detalle de cargos de prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_detalle_cargos_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Detalle Rechazos Prorroga #########
#############################################
@app_v1.route('/prorrogas/rechazos/detalle', methods=['GET'])
def obtener_detalle_rechazos_prorroga():
    """
    Endpoint para obtener el detalle de rechazos de prórroga
    """
    id_prorroga = request.args.get('id_prorroga', default=None, type=int)
    response, status_code = servicios.get_detalle_rechazos_prorroga(id_prorroga)
    return jsonify(response), status_code

#############################################
######    Cantidad Operaciones Prorrogas por RUT #
#############################################
@app_v1.route('/prorrogas/operaciones/cantidad', methods=['GET'])
def obtener_cantidad_operaciones_prorrogas_por_rut():
    """
    Endpoint para obtener la cantidad de operaciones prorrogadas por RUT
    """
    rut = request.args.get('rut', default=None, type=int)
    response, status_code = servicios.get_cantidad_operaciones_prorrogas_por_rut(rut)
    return jsonify(response), status_code

#############################################
######    Cantidad Operaciones por RUT ######
#############################################
@app_v1.route('/operaciones/cantidad', methods=['GET'])
def obtener_cantidad_operaciones_por_rut():
    """
    Endpoint para obtener la cantidad de operaciones por RUT
    """
    rut = request.args.get('rut', default=None, type=int)
    response, status_code = servicios.get_cantidad_operaciones_por_rut(rut)
    return jsonify(response), status_code

#############################################
######    Prorrogas Firmadas      ###########
#############################################
@app_v1.route('/prorrogas/firmadas', methods=['GET'])
def obtener_prorrogas_firmadas():
    """
    Endpoint para obtener las prórrogas firmadas
    """
    id_usuario = request.args.get('id_usuario', default=None, type=int)
    id_prorroga = request.args.get('id_prorroga', default=-1, type=int)
    response, status_code = servicios.get_prorrogas_firmadas(id_usuario, id_prorroga)
    return jsonify(response), status_code

#############################################
######    Todas Prorrogas Firmadas ##########
#############################################
@app_v1.route('/prorrogas/firmadas/todas', methods=['GET'])
def obtener_todas_prorrogas_firmadas():
    """
    Endpoint para obtener todas las prórrogas firmadas
    """
    response, status_code = servicios.get_todas_prorrogas_firmadas()
    return jsonify(response), status_code

#############################################
######    Prorrogas Firmas Usuario ##########
#############################################
@app_v1.route('/prorrogas/firmas', methods=['GET'])
def obtener_prorrogas_firmas():
    """
    Endpoint para obtener prórrogas firmas del usuario
    """
    id_usuario = request.args.get('id_usuario', default=None, type=int)
    response, status_code = servicios.get_prorrogas_firmas(id_usuario)
    return jsonify(response), status_code

#############################################
######    Todas Prorrogas Firmas ###########
#############################################
@app_v1.route('/prorrogas/firmas/todas', methods=['GET'])
def obtener_todas_prorrogas_firmas():
    """
    Endpoint para obtener todas las prórrogas firmas
    """
    response, status_code = servicios.get_todas_prorrogas_firmas()
    return jsonify(response), status_code


#TODO: Crear el endpoint para el procedure en PCK_PRORROGA.GRABARJUSTIFICACIONPRORROGA methods =  UPDATE(PUT O PATCH ? )

app.register_blueprint(app_v1)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])
