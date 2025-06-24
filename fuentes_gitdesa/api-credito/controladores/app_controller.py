from flask import request, jsonify, g
from utils.decorador import handle_exceptions
from .controlador_base import BaseController
from servicios import servicios


class CreditosProrrogaController(BaseController):

    def __init__(self):
        super()

    @handle_exceptions
    def health(self):
        return jsonify("OK"), 200

    @handle_exceptions
    def obtener_credito(self):
        """
        Endpoint para obtener creditos
        """
        credito = request.args.get('credito',default=-1,type=int)
        estado = request.args.get('estado',default=-1,type=int)
        rut = request.args.get('rut',type=int)
        prorrogados = request.args.get('prorrogados',default='N',type=str)
        response, status_code = servicios.get_credito(credito,rut,estado,prorrogados)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code


    #############################################
    ######    Bloqueo Credito         ###########
    #############################################
    @handle_exceptions
    def obtener_credito_bloqueo(self):
        """
        Endpoint para obtener bloqueos de crédito
        """
        operacion = request.args.get('operacion', default=None, type=int)
        estado = request.args.get('estado', default='0', type=str)
        judicial = request.args.get('judicial', default='0', type=str)
        response, status_code = servicios.get_credito_bloqueo(operacion, estado, judicial)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code



    #############################################
    ######    Cuotas                  ###########
    #############################################
    @handle_exceptions
    def obtener_cuotas(self):
        """
        Endpoint para obtener cuotas de crédito
        """
        operacion = request.args.get('operacion', default=None, type=int)
        peso = request.args.get('peso', default='N', type=str)
        response, status_code = servicios.get_cuotas(operacion, peso)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Movimientos             ###########
    #############################################
    @handle_exceptions
    def obtener_movimientos(self):
        """
        Endpoint para obtener movimientos de crédito
        """
        credito = request.args.get('credito', default=None, type=int)
        response, status_code = servicios.obtener_movimientos(credito)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Operaciones Cliente     ###########
    #############################################
    @handle_exceptions
    def obtener_operaciones_cliente(self):
        """
        Endpoint para obtener operaciones de cliente
        """
        todos = request.args.get('todos', default=None, type=str)
        fecha = request.args.get('fecha', default=None, type=str)
        cliente = request.args.get('cliente', default=0, type=int)
        operacion = request.args.get('operacion', default=0, type=int)
        response, status_code = servicios.obtener_operaciones_cliente(todos, fecha, cliente, operacion)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Prorroga        ###########
    #############################################
    @handle_exceptions
    def obtener_detalle_prorroga(self):
        """
        Endpoint para obtener detalle de prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.obtener_detalle_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Rechazos Prorroga       ###########
    #############################################
    @handle_exceptions
    def obtener_rechazos_prorroga(self):
        """
        Endpoint para obtener rechazos de prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_rechazos_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Cuotas Prorrogas        ###########
    #############################################
    @handle_exceptions
    def obtener_cuotas_prorrogas(self):
        """
        Endpoint para obtener cuotas de prórrogas
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        cuota_desde = request.args.get('cuota_desde', default=None, type=int)
        cuota_hasta = request.args.get('cuota_hasta', default=None, type=int)
        response, status_code = servicios.get_cuotas_prorrogas(id_prorroga, cuota_desde, cuota_hasta)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Cuotas Prorrogas Posterior ########
    #############################################
    @handle_exceptions
    def obtener_cuotas_prorrogas_posterior(self):
        """
        Endpoint para obtener cuotas posteriores de prórrogas
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_cuotas_prorrogas_posterior(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Cuotas Prorrogas Posterior #
    #############################################
    @handle_exceptions
    def obtener_detalle_cuotas_prorrogas_posterior(self):
        """
        Endpoint para obtener detalle de cuotas posteriores de prórrogas
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_detalle_cuotas_prorrogas_posterior(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Cargos Prorroga         ###########
    #############################################
    @handle_exceptions
    def obtener_cargos_prorroga(self):
        """
        Endpoint para obtener cargos de prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_cargos_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Creditos Prorroga       ###########
    #############################################
    @handle_exceptions
    def obtener_creditos_prorroga(self):
        """
        Endpoint para obtener créditos de prórroga
        """
        rut = request.args.get('rut', default=None, type=int)
        response, status_code = servicios.get_creditos_prorroga(rut)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Rechazo Prorroga Usuario ##########
    #############################################
    @handle_exceptions
    def obtener_rechazo_prorroga_usuario(self):
        """
        Endpoint para obtener rechazo de prórroga por usuario
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        id_usuario = request.args.get('id_usuario', default=None, type=int)
        response, status_code = servicios.get_rechazo_prorroga_usuario(id_prorroga, id_usuario)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Parametros              ###########
    #############################################
    @handle_exceptions
    def obtener_parametros(self):
        """
        Endpoint para obtener parámetros
        """
        response, status_code = servicios.get_parametros()
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Grupo Prorrogas         ###########
    #############################################
    @handle_exceptions
    def obtener_grupo_prorrogas(self):
        """
        Endpoint para obtener grupo de prórrogas
        """
        codigo = request.args.get('codigo', default=None, type=int)
        response, status_code = servicios.get_grupo_prorrogas(codigo)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Cuota Posterior Prorroga ##
    #############################################
    @handle_exceptions
    def obtener_detalle_cuota_posterior_prorroga(self):
        """
        Endpoint para obtener detalle de cuotas posteriores de la prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_detalle_cuota_posterior_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Cuota Anterior Prorroga ###
    #############################################
    @handle_exceptions
    def obtener_detalle_cuota_anterior_prorroga(self):
        """
        Endpoint para obtener detalle de cuotas anteriores de la prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_detalle_cuota_anterior_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Cargos Prorroga ###########
    #############################################
    @handle_exceptions
    def obtener_detalle_cargos_prorroga(self):
        """
        Endpoint para obtener el detalle de cargos de prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_detalle_cargos_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Detalle Rechazos Prorroga #########
    #############################################
    @handle_exceptions
    def obtener_detalle_rechazos_prorroga(self):
        """
        Endpoint para obtener el detalle de rechazos de prórroga
        """
        id_prorroga = request.args.get('id_prorroga', default=None, type=int)
        response, status_code = servicios.get_detalle_rechazos_prorroga(id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Cantidad Operaciones Prorrogas por RUT #
    #############################################
    @handle_exceptions
    def obtener_cantidad_operaciones_prorrogas_por_rut(self):
        """
        Endpoint para obtener la cantidad de operaciones prorrogadas por RUT
        """
        rut = request.args.get('rut', default=None, type=int)
        response, status_code = servicios.get_cantidad_operaciones_prorrogas_por_rut(rut)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Cantidad Operaciones por RUT ######
    #############################################
    @handle_exceptions
    def obtener_cantidad_operaciones_por_rut(self):
        """
        Endpoint para obtener la cantidad de operaciones por RUT
        """
        rut = request.args.get('rut', default=None, type=int)
        response, status_code = servicios.get_cantidad_operaciones_por_rut(rut)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Prorrogas Firmadas      ###########
    #############################################
    @handle_exceptions
    def obtener_prorrogas_firmadas(self):
        """
        Endpoint para obtener las prórrogas firmadas
        """
        id_usuario = request.args.get('id_usuario', default=None, type=int)
        id_prorroga = request.args.get('id_prorroga', default=-1, type=int)
        response, status_code = servicios.get_prorrogas_firmadas(id_usuario, id_prorroga)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Todas Prorrogas Firmadas ##########
    #############################################
    @handle_exceptions
    def obtener_todas_prorrogas_firmadas(self):
        """
        Endpoint para obtener todas las prórrogas firmadas
        """
        response, status_code = servicios.get_todas_prorrogas_firmadas()
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Prorrogas Firmas Usuario ##########
    #############################################
    @handle_exceptions
    def obtener_prorrogas_firmas(self):
        """
        Endpoint para obtener prórrogas firmas del usuario
        """
        id_usuario = request.args.get('id_usuario', default=None, type=int)
        response, status_code = servicios.get_prorrogas_firmas(id_usuario)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    #############################################
    ######    Todas Prorrogas Firmas ###########
    #############################################
    @handle_exceptions
    def obtener_todas_prorrogas_firmas(self):
        """
        Endpoint para obtener todas las prórrogas firmas
        """
        response, status_code = servicios.get_todas_prorrogas_firmas()
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code

    @handle_exceptions
    def validar_existencia_prorroga(self):
        """
        Endpoint para obtener todas las prórrogas firmas
        """

        operacion= request.args.get('operacion',type=int)
        response, status_code = servicios.get_validar_prorroga(operacion)
        response, status_code = self._format_response(response,status_code)
        return jsonify(response), status_code


