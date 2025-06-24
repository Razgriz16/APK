from flask import Blueprint
from controladores import app_controller


app_v1 = Blueprint('app_v1',__name__)

cta_ahorro_controller = app_controller.CuentaAhorroController()


@app_v1.route('/cuenta-ahorro', methods=['GET'])
def obtener_cliente():
    return cta_ahorro_controller.obtener_cliente()

@app_v1.route('/cuenta-ahorro/movimientos', methods=['GET'])
def obtener_movimientos():
    return cta_ahorro_controller.obtener_movimientos()

@app_v1.route('/cuenta-ahorro/cuenta/bloqueo-dbuaf',methods=['GET'])
def verificar_bloqueo_dbf_uaf():
    return cta_ahorro_controller.verificar_bloqueo_dbf_uaf()

@app_v1.route('/cuenta-ahorro/ultimos-movimientos',methods=['GET'])
def obtener_ultimos_movimientos():
    return cta_ahorro_controller.obtener_ultimos_movimientos()

