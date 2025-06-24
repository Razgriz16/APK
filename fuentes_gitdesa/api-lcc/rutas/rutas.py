from flask import Blueprint
from controladores import app_controller
import funciones_db

app_v1 = Blueprint('app_v1',__name__)

# Intancia del controller
lcc_controller = app_controller.LccController()

@app_v1.route('/lineacc',methods=['GET'])
def get_lineacc():
    """
    Endpoint para obtener la informacion de la lineacc
    """
    return lcc_controller.obtener_lineacc()

