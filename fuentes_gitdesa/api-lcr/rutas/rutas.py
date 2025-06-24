from flask import Blueprint
from controladores import app_controller
import funciones_db

app_v1 = Blueprint('app_v1',__name__)

# Intancia del controller
lcr_controller = app_controller.LcrController()

@app_v1.route('/lineacr',methods=['GET'])
def get_lineacr():
    """
    Endpoint para obtener la informacion de la lineacr
    """
    return lcr_controller.obtener_lineacr()

@app_v1.route('/movimientos-lineacr',methods=['GET'])
def get_mov_lineacr():
    """
    Endpoint para obtener movimientos de la lineacr
    """
    return lcr_controller.obtener_mov_lineacr()

