from flask import Blueprint
from controladores import app_controller


app_v1 = Blueprint('app_v1',__name__)

dap_controller = app_controller.DapController()


@app_v1.route('/recuperar-dap', methods=['GET'])
def recuperar_operaciones_dap():
    return dap_controller.recuperar_operaciones()

