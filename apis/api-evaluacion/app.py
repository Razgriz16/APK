#from funciones_db import create_session_pool,pkg_exe_par_cursor,pkg_exe_error_msg_cursor import funciones_db
from  servicios import servicios 
from flask import Flask, request, jsonify, current_app
import yaml
import cx_Oracle
from cx_Oracle import SessionPool


app = Flask(__name__)

################################################# # Cargar la configuración desde el archivo YAML #
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
######    Recuperar  Credito        #########
#############################################
@app.route('/v1/creditos', methods=['GET'])
def obtener_credito():
    """
    Endpoint para obtener creditos
    """
    #Params necesarios
    credito = request.args.get('credito',default=-1,type=int)
    estado = request.args.get('estado',default=-1,type=int)
    rut = request.args.get('rut',default=-1,type=int)
    prorrogados = request.args.get('prorrogados',default='N',type=str)

    #current_app.logger.info(request.args)
    #current_app.logger.info(type(credito))

    response, status_code = servicios.obtener_credito(credito,rut,estado,prorrogados)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


#############################################
######    Recuperar  Cuotas         #########
#############################################
@app.route('/v1/creditos/cuotas', methods=['GET'])
def obtener_cuotas():
    """
    Endpoint para obtener cuotas
    """
    #Params necesarios
    operacion = request.args.get('operacion',type=int)
    peso = request.args.get('peso',default='N',type=str)

    current_app.logger.info(request.args)

    response, status_code = servicios.obtener_cuotas(operacion,peso)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


#############################################
######    Recuperar Movimientos     #########
#############################################
@app.route('/v1/creditos/movimientos', methods=['GET'])
def obtener_movimientos():
    """
    Endpoint para obtener movimientos
    """
    #Params necesarios
    credito = request.args.get('credito',type=int)

    current_app.logger.info(request.args)

    response, status_code = servicios.obtener_movimientos(credito)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code



#####################################################
######    Recuperar  Credito Bloqueos        ########
#####################################################
@app.route('/v1/creditos/bloqueos', methods=['GET'])
def obtener_credito_bloqueo():
    """
    Endpoint para obtener creditos bloqueados
    """
    #Params necesarios
    operacion = request.args.get('operacion',type=int)
    estado = request.args.get('estado',default='0',type=str)
    judicial = request.args.get('judicial',default='0',type=str)

    #Usar servicio
    response, status_code = servicios.obtener_credito_bloqueo(operacion,estado,judicial)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#############################################################################
# Queries de DataConDAO.java
###################################################
######    Recuperar Detalle Prorrogas       #######
###################################################
@app.route('/v1/creditos/prorroga/detalle', methods=['GET'])
def obtener_detalle_prorroga():
    """
    Endpoint para obtener el detalle de prorrogas
    """
    #Params necesarios
    id_prorroga = request.args.get('idprorroga',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_prorroga(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


####################################################
#######    Recuperar Rechazos Prorrogas       ######
####################################################
#@app.route('/v1/creditos/prorrogas/rechazos', methods=['GET'])
#def obtener_rechazo_prorroga():
#    """
#    Endpoint para obtener rechazos prorroga
#    """
#    #Params necesarios
#    id_prorroga = request.args.get('idprorroga',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_rechazos_prorroga(id_prorroga)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#
#

#
#
###########################################################
#######    Recuperar Cuotas Posteriores Prorrogas     #####
###########################################################
@app.route('/v1/creditos/prorroga/cuotas/posterior', methods=['GET'])
def obtener_cuota_prorroga_posterior():
    """
    Endpoint para obtener las cutoas prorroga
    """
    #Params necesarios
    id_prorroga = request.args.get('idprorroga',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_cuotas_prorrogas_posterior(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

##############################################################
#######    Recuperar Detalle Cuotas Posterios Prorroga    ####
##############################################################
@app.route('/v1/creditos/prorroga/cuotas/posterior/detalle', methods=['GET'])
def obtener_cuota_prorroga_posterior_detalle():
    """
    Endpoint para obtener las cuotas prorroga
    """
    #Params necesarios
    id_prorroga = request.args.get('idprorroga',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_cuotas_prorrogas_posterior(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

##############################################
#######    Recuperar Cargos Prorroga    ######
##############################################
#@app.route('/v1/creditos/prorrogas/cargos',methods=['GET'])
#def obtener_cargos_prorroga():
#    """
#    Endpoint para obtener cargos prorroga
#    """
#    #Params necesarios
#    id_prorroga = request.args.get('idprorroga',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_cargos_prorroga(id_prorroga)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#
################################################
#######    Recuperar Creditos Prorroga    ######
################################################
#@app.route('/v1/creditos/prorroga',methods=['GET'])
#def obtener_credito_prorroga():
#    """
#    Endpoint para obtener credito prorroga 
#    """
#    #Params necesarios
#    rut = request.args.get('rut',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_creditos_prorroga(rut)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#
################################################
#######    Recuperar Rechazos Prorroga    ######
################################################
#@app.route('/v1/creditos/prorroga/rechazos',methods=['GET'])
#def obtener_rechazos_prorroga():
#    """
#    Endpoint para obtener rechazo prorroga
#    """
#    #Params necesarios
#    id_prorroga = request.args.get('idprorroga',type=int)
#    id_usuario  = request.args.get('idusuario',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_rechazo_prorroga(id_prorroga,id_usuario)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#
############################################
#######    Recuperar Linea Credito    ######
############################################
#@app.route('/v1/creditos/linea-credito',methods=['GET'])
#def obtener_linea_credito():
#    """
#    Endpoint para obtener linea credito 
#    """
#    #Params necesarios
#    rut  = request.args.get('rut',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_linea_credito(rut)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code

#############################################################################

#######################################
######    Recuperar Parametros   ######
#######################################
@app.route('/v1/creditos/prorroga/parametros',methods=['GET'])
def obtener_credito_parametros():
    """
    Endpoint para obtener los paremetros de prorrogas
    """

    #Usar servicio
    response, status_code = servicios.obtener_parametros()

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#############################################################
######    Recuperar Parametros De Grupos De Prorroga   ######
#############################################################
@app.route('/v1/creditos/prorroga/parametros/grupos',methods=['GET'])
def obtener_grupo_prorrogas():
    """
    Endpoint para obtener los grupos de prorroga
    """
    #Params necesarios
    codigo  = request.args.get('codigo',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_grupo_prorrogas(codigo)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


###############################################
######    Recuperar  Datos De Prorroga   ######
###############################################
#@app.route('/v1/creditos/prorroga/detalle',methods=['GET'])
#def obtener_datos_prorroga():
#    """
#    Endpoint para obtener datos de prorroga
#    """
#    #Params necesarios
#    id_prorroga  = request.args.get('idprorroga',type=int)
#    estado = request.args.get('estado',default=-1,type=int)
#    sucursal = request.args.get('sucursal',default=-1,type=int)
#    credito = request.args.get('credito',default=-1,type=int)
#    rut = request.args.get('credito',default=-1,type=int)
#    considerada = request.args.get('usr-solicita',default=-1,type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_detalle_prorroga(id_prorroga,estado,sucursal,credito,rut,considerada)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#
#
###################################################################
######    Recuperar  Datos De Cuota Posterior A La Prorroga  ######
###################################################################
@app.route('/v1/creditos/prorroga/cuotas-posterior/detalle',methods=['GET'])
def obtener_datos_cuotas_posterior():
    """
    Endpoint para obtener datos de las cuotas posteriores a la prorroga 
    """
    #Params necesarios
    id_prorroga  = request.args.get('idprorroga',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_cuota_posterior_prorroga(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###################################################################
######    Recuperar  Datos De Cuota Anterior A La Prorroga  ######
###################################################################
@app.route('/v1/creditos/prorroga/cuotas-anterior/detalle',methods=['GET'])
def obtener_datos_cuotas_anterior():
    """
    Endpoint para obtener datos las cuotas anteriores a la prorroga
    """
    #Params necesarios
    id_prorroga  = request.args.get('idprorroga',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_cuota_anterior_prorroga(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

########################################################
######    Recuperar  Datos De Cargos De Prorroga  ######
########################################################
@app.route('/v1/creditos/prorroga/cargos/detalle',methods=['GET'])
def obtener_datos_cargos_prorroga():
    """
    Endpoint para obtener datos los cargos de prorroga 
    """
    #Params necesarios
    id_prorroga  = request.args.get('idprorroga',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_cargos_prorroga(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#########################################################################
######    Recuperar  Datos De Rechazos De Prorroga, Sin privlegios  #####
#########################################################################
@app.route('/v1/creditos/prorroga/rechazos/detalle',methods=['GET'])
def obtener_datos_rechazos_prorroga():
    """
    Endpoint para obtener datos los rechazos de prorroga
    """
    #Params necesarios
    id_prorroga  = request.args.get('idprorroga',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_detalle_rechazos_prorroga(id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#########################################################
######    Recuperar  Datos De Rechazos De Usuario  ######
#########################################################
@app.route('/v1/creditos/prorroga/rechazos-usuario/detalle',methods=['GET'])
def obtener_datos_rechazos_usuario():
    """
    Endpoint para obtener datos los rechazos de prorroga
    """
    #Params necesarios
    id_prorroga  = request.args.get('idprorroga',type=int)
    id_usuario  = request.args.get('usuario',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_rechazo_prorroga_usuario(id_prorroga,id_usuario)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code


##############################################################
######    Recuperar Rechazos Prorroga Con Privilegios   ######
##############################################################

#@app.route('/v1/creditos/prorroga/rechazos/detalle',methods=['GET'])
#def obtener_rechazos_prorroga():
#    """
#    Endpoint para obtener rechazo prorroga
#    """
#    #Params necesarios
#    id_prorroga = request.args.get('idprorroga',type=int)
#    id_usuario  = request.args.get('idusuario',type=int)
#
#    #Usar servicio
#    response, status_code = servicios.obtener_rechazo_prorroga(id_prorroga,id_usuario)
#
#    # Devolver la respuesta en formato JSON
#    return jsonify(response), status_code
#


########################################################################
######    Recuperar  Cantidad De Operaciones Prorrogadas Por Rut  ######
########################################################################
@app.route('/v1/creditos/prorroga/operaciones',methods=['GET'])
def obtener_operaciones_prorrogadas():
    """
    Endpoint para obtener la cantidad de operaciones prorrogadas por rut
    """
    #Params necesarios
    rut  = request.args.get('rut',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_cantidad_operaciones_prorrogas_por_rut(rut)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code
##################################################
#######    Recuperar Cuotas Prorrogas       ######
##################################################
@app.route('/v1/creditos/prorroga/cuotas/anterior', methods=['GET'])
def obtener_cuota_prorroga():
    """
    Endpoint para obtener las cutoas prorroga
    """
    #Params necesarios
    id_prorroga = request.args.get('idprorroga',type=int)
    cuota_desde = request.args.get('cuota-desde',type=str)
    cuota_hasta = request.args.get('cuota-hasta',type=str)

    #Usar servicio
    response, status_code = servicios.obtener_cuotas_prorrogas(id_prorroga,cuota_desde,cuota_hasta)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###############################################
######    Recuperar Creditos Prorroga    ######
###############################################
@app.route('/v1/creditos/prorroga',methods=['GET'])
def obtener_credito_prorroga():
    """
    Endpoint para obtener credito prorroga 
    """
    #Params necesarios
    rut = request.args.get('rut',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_creditos_prorroga(rut)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

############################################################
######    Recuperar  Cantidad De Operaciones Por Rut  ######
############################################################
@app.route('/v1/creditos/operaciones',methods=['GET'])
def obtener_operaciones():
    """
    Endpoint para obtener la cantidad de operaciones por rut
    """
    #Params necesarios
    rut  = request.args.get('rut',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_cantidad_operaciones_por_rut(rut)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

###############################################
######    Recuperar Prorrogas Firmadas   ######
###############################################
@app.route('/v1/creditos/prorrogas-firmadas/detalle',methods=['GET'])
def obtener_prorrogas_firmadas():
    """
    Endpoint para obtener prorrogas firmadas
    """
    #Params necesarios
    id_usuario  = request.args.get('idusuario',type=int)
    id_prorroga  = request.args.get('idprorroga',default=-1,type=int)

    #Usar servicio
    response, status_code = servicios.obtener_prorrogas_firmadas(id_usuario,id_prorroga)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#########################################################
######    Recuperar Todas Las Prorrogas Firmadas   ######
#########################################################
@app.route('/v1/creditos/prorrogas-firmadas',methods=['GET'])
def obtener_todas_prorrogas_firmadas():
    """
    Endpoint para obtener todas las  prorrogas firmadas
    """
    
    response, status_code = servicios.obtener_todas_prorrogas_firmadas()

    return jsonify(response), status_code

####################################################
######    Recuperar Prorrogas Firma detalle   ######
####################################################
@app.route('/v1/creditos/prorrogas-firmas/detalle',methods=['GET'])
def obtener_prorrogas_firmas():
    """
    Endpoint para obtener prorrogas firmadas
    """
    #Params necesarios
    id_usuario  = request.args.get('idusuario',type=int)

    #Usar servicio
    response, status_code = servicios.obtener_prorrogas_firmas(id_usuario)

    # Devolver la respuesta en formato JSON
    return jsonify(response), status_code

#########################################################
######    Recuperar Todas Las Prorrogas Firmadas   ######
#########################################################
@app.route('/v1/creditos/prorrogas-firmas',methods=['GET'])
def obtener_todas_prorrogas_firmas():
    """
    Endpoint para obtener todas las  prorrogas firmadas
    """
    
    response, status_code = servicios.obtener_todas_prorrogas_firmas()

    return jsonify(response), status_code




#TODO: Crear el endpoint para el procedure en PCK_PRORROGA.GRABARJUSTIFICACIONPRORROGA methods =  UPDATE(PUT O PATCH ? )





if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=app_config['port'], debug=app_config['debug'])
