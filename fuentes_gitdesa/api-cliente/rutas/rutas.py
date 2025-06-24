from flask import Blueprint
from controladores import app_controller

app_v1 = Blueprint('app_v1',__name__)

#Instancia del controller de clientes
clientes_controller = app_controller.ClientesController()

@app_v1.route('/auth/login', methods=['POST'])
def login_cliente():
    return clientes_controller.login()

@app_v1.route('/cliente', methods=['GET'])
def get_cliente():
    return clientes_controller.obtener_usuario_por_rut()

@app_v1.route('/cliente/direccion', methods=['GET'])
def get_direccion_cliente():
    return clientes_controller.obtener_direccion_cliente()

@app_v1.route('/cliente/telefono', methods=['GET'])
def get_telefono_cliente():
    return clientes_controller.obtener_telefono_cliente()

@app_v1.route('/cliente/telefono-verificado', methods=['GET'])
def get_telefono_verificado():
    return clientes_controller.obtener_telefono_verificado_cliente()

@app_v1.route('/cliente/correo', methods=['GET'])
def get_correo_cliente():
    return clientes_controller.obtener_correo_cliente()

@app_v1.route('/funcionario/sucursal', methods=['GET'])
def get_sucursal_funcionario():
    return clientes_controller.obtener_sucursal_funcionario()
