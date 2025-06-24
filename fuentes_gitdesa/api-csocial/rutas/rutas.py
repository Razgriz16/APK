from flask import Blueprint
from controladores import app_controller


app_v1 = Blueprint('app_v1',__name__)

csocial_controller = app_controller.CsocialController()


@app_v1.route('/cuenta-csocial', methods=['GET'])
def obtener_cliente():
    return csocial_controller.obtener_cliente()

#@app_v1.route('/cuenta-ahorro/cuenta/bloqueo-dbuaf',methods=['GET'])
#def verificar_bloqueo_dbf_uaf():
#    return cta_ahorro_controller.verificar_bloqueo_dbf_uaf()

@app_v1.route('/cuenta-csocial/ultimos-movimientos',methods=['GET'])
def obtener_ultimos_movimientos():
    return csocial_controller.obtener_ultimos_movimientos()

