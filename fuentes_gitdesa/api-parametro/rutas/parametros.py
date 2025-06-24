from flask import Blueprint
from controladores import app_controller
import funciones_db

app_v1 = Blueprint('app_v1', __name__)

# Instanciar el controlador
prorrogas_controller = app_controller.ParametrosController()

@app_v1.route('/sucursales/activas', methods=['GET'])
def get_sucursales_activas():
    """
    Endpoint para obtener las sucursales activas 
    """
    return prorrogas_controller.obtener_sucursales_activas()


@app_v1.route('/sucursal', methods=['GET'])
def get_sucursal_por_codigo():
    """
    Endpoint para obtener las sucursales
    """
    return prorrogas_controller.obtener_sucursal_por_codigo()

@app_v1.route('/comunas', methods=['GET'])
def get_comunas():
    """
    Endpoint para obtener comunas
    """
    return prorrogas_controller.obtener_comunas()

@app_v1.route('/ciudades', methods=['GET'])
def get_ciudades():
    """
    Endpoint para obtener ciudades
    """
    return prorrogas_controller.obtener_ciudades()

@app_v1.route('/parametros-sgt', methods=['GET'])
def get_parametros_sgt():
    """
    Endpoint para obtener parametros
    """
    return prorrogas_controller.obtener_parametros_sgt()

@app_v1.route('/bloqueo', methods=['GET'])
def get_bloqueo():
    """
    Endpoint para obtener parametros
    """
    return prorrogas_controller.obtener_credito_bloqueado_test()

@app_v1.route('/cliente',methods=['GET'])
def get_cliente():
    return prorrogas_controller.obtener_cliente_test()

