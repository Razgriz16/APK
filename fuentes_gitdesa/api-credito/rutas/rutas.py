from flask import Blueprint
from controladores import app_controller


app_v1=Blueprint('app_v1',__name__)

credito_controller = app_controller.CreditosProrrogaController()


@app_v1.route('/health', methods=['GET'])
def health():
    return credito_controller.health()

@app_v1.route('/creditos', methods=['GET'])
def obtener_credito():
    return credito_controller.obtener_credito()

@app_v1.route('/creditos/bloqueo', methods=['GET'])
def obtener_credito_bloqueo():
    return credito_controller.obtener_credito_bloqueo()

@app_v1.route('/creditos/cuotas', methods=['GET'])
def obtener_cuotas():
    return credito_controller.obtener_cuotas()

@app_v1.route('/creditos/movimientos', methods=['GET'])
def obtener_movimientos():
    return credito_controller.obtener_movimientos()

@app_v1.route('/operaciones/cliente', methods=['GET'])
def obtener_operaciones_cliente():
    return credito_controller.obtener_operaciones_cliente()

@app_v1.route('/prorrogas/detalle', methods=['GET'])
def obtener_detalle_prorroga():
    return credito_controller.obtener_detalle_prorroga()
    
@app_v1.route('/prorrogas/rechazos', methods=['GET'])
def obtener_rechazos_prorroga():
    return credito_controller.obtener_rechazos_prorroga()

@app_v1.route('/prorrogas/cuotas', methods=['GET'])
def obtener_cuotas_prorrogas():
    return credito_controller.obtener_cuotas_prorrogas()

@app_v1.route('/prorrogas/cuotas/posterior', methods=['GET'])
def obtener_cuotas_prorrogas_posterior():
    return credito_controller.obtener_cuotas_prorrogas_posterior()

@app_v1.route('/prorrogas/cuotas/posterior/detalle', methods=['GET'])
def obtener_detalle_cuotas_prorrogas_posterior():
    return credito_controller.obtener_detalle_cuotas_prorrogas_posterior()

@app_v1.route('/prorrogas/cargos', methods=['GET'])
def obtener_cargos_prorroga():
    return credito_controller.obtener_cargos_prorroga()

@app_v1.route('/prorrogas/creditos', methods=['GET'])
def obtener_creditos_prorroga():
    return credito_controller.obtener_creditos_prorroga()

@app_v1.route('/prorrogas/rechazos/usuario', methods=['GET'])
def obtener_rechazo_prorroga_usuario():
    return credito_controller.obtener_rechazo_prorroga_usuario()

@app_v1.route('/parametros', methods=['GET'])
def obtener_parametros():
    return credito_controller.obtener_parametros()

@app_v1.route('/prorrogas/grupo', methods=['GET'])
def obtener_grupo_prorrogas():
    return credito_controller.obtener_grupo_prorrogas()

@app_v1.route('/prorrogas/cuota/posterior/detalle', methods=['GET'])
def obtener_detalle_cuota_posterior_prorroga():
    return credito_controller.obtener_detalle_cuota_posterior_prorroga()

@app_v1.route('/prorrogas/cuota/anterior/detalle', methods=['GET'])
def obtener_detalle_cuota_anterior_prorroga():
    return credito_controller.obtener_detalle_cuota_anterior_prorroga()

@app_v1.route('/prorrogas/cargos/detalle', methods=['GET'])
def obtener_detalle_cargos_prorroga():
    return credito_controller.obtener_detalle_cargos_prorroga()

@app_v1.route('/prorrogas/rechazos/detalle', methods=['GET'])
def obtener_detalle_rechazos_prorroga():
    return credito_controller.obtener_detalle_rechazos_prorroga()

@app_v1.route('/prorrogas/operaciones/cantidad', methods=['GET'])
def obtener_cantidad_operaciones_prorrogas_por_rut():
    return credito_controller.obtener_cantidad_operaciones_prorrogas_por_rut()

@app_v1.route('/operaciones/cantidad', methods=['GET'])
def obtener_cantidad_operaciones_por_rut():
    return credito_controller.obtener_cantidad_operaciones_por_rut()

@app_v1.route('/prorrogas/firmadas', methods=['GET'])
def obtener_prorrogas_firmadas():
    return credito_controller.obtener_prorrogas_firmadas()

@app_v1.route('/prorrogas/firmadas/todas', methods=['GET'])
def obtener_todas_prorrogas_firmadas():
    return credito_controller.obtener_todas_prorrogas_firmadas()

@app_v1.route('/prorrogas/firmas', methods=['GET'])
def obtener_prorrogas_firmas():
    return credito_controller.obtener_prorrogas_firmas()

@app_v1.route('/prorrogas/firmas/todas', methods=['GET'])
def obtener_todas_prorrogas_firmas():
    return credito_controller.obtener_todas_prorrogas_firmas()

@app_v1.route('/prorrogas/existe', methods=['GET'])
def validar_existencia_prorroga():
    return credito_controller.validar_existencia_prorroga()


