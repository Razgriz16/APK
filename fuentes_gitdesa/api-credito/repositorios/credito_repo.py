class CreditoRepository():
    def __init__(self,funciones_db):
        self.funciones_db=funciones_db
    def obtener_credito(self,credito,rut,estado,prorrogados):
        package_name="PCK_CREDITO"
        procedure_name="RECUPERACREDITOS"
        params = [credito,estado,rut,prorrogados]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_credito_bloqueo(self,operacion,estado,judicial):
        package_name="PCK_CREDITO"
        procedure_name="CRCRECBLOQUEOS"
        params = [operacion,estado,judicial]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code


    def obtener_cuotas(self,operacion,peso):
        package_name="PCK_CREDITO"
        procedure_name="RECUPERARCUOTAS"
        collection_type_name="CREDITO.CRC_CUOTAS_CREDITO_TAB"
        params = {
            "P_OPERACION":operacion,
            "P_PESO":peso,
        }
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_collection(procedure_name,package_name,params,collection_type_name)
        return response, status_code

    def obtener_movimientos(self,credito):
        package_name="PCK_CREDITO"
        procedure_name="RECUPERARMOVIMIENTOS"
        params = [credito]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_operaciones_cliente(self,todos,fecha,cliente,operacion):
        package_name="CARTERAVENCIDA.PCK_CVENCIDA"
        procedure_name="CVERECOPERACIONESCLIENTE"
        collection_type_name="CARTERAVENCIDA.CVE_OPERACIONES_TAB"
        params = {
            "P_CLIENTE":cliente,
            "P_OPERACION":operacion,
            "P_TODOS":todos,
            "P_FECHAPROCESO":fecha,
        }
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_collection(procedure_name,package_name,params,collection_type_name)
        return response, status_code

    ################################################
    ## PRORROGA - Queries de DataConDAO.java   #####
    ################################################
    def obtener_detalle_prorroga(self,id_prorroga):
        package_name="PCK_CREDITO"
        procedure_name="RECPRORROGA"
        params = [id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_rechazos_prorroga(self,id_prorroga):
        package_name="PCK_CREDITO"
        procedure_name="RECRECHAZOSPRORROGA"
        params = [id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code


    def obtener_cuotas_prorrogas(self,id_prorroga,cuota_desde,cuota_hasta):
        package_name="PCK_CREDITO"
        procedure_name="RECCUOTASPRORROGA"
        params = [id_prorroga,cuota_desde,cuota_hasta]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_cuotas_prorrogas_posterior(self,id_prorroga):
        package_name="PCK_CREDITO"
        procedure_name="RECCUOTASPOSTPRORROGA"
        params = [id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_detalle_cuotas_prorrogas_posterior(self,id_prorroga):
        package_name="PCK_CREDITO"
        procedure_name="RECDETALLECUOTAPOSTPRORROGA"
        params = [id_prorroga]
        #current_app.logger.info(params) #Log de params
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_cargos_prorroga(self,id_prorroga):
        package_name="PCK_CREDITO"
        procedure_name="RECCARGOSPRORROGA"
        params = [id_prorroga]
        #current_app.logger.info(params) #Log de params
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_creditos_prorroga(self,rut):
        package_name="PCK_CREDITO"
        procedure_name="RECCREDITOSPRORROGA"
        params = [rut]
        #current_app.logger.info(params) #Log de params
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_rechazo_prorroga_usuario(self,id_prorroga,id_usuario):
        package_name="PCK_CREDITO"
        procedure_name="RECRECHAZOUSUARIO"
        params = [id_prorroga,id_usuario]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_linea_credito(self,rut):
        package_name="PCK_CREDITO"
        procedure_name="RECLINEACC"
        params = [rut]
        #current_app.logger.info(params) #Log de params
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_parametros(self,):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARPARAMETROS"
        response , status_code = self.funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)
        return response, status_code

    def obtener_grupo_prorrogas(self,codigo):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARPARAMETROSGRUPO"
        params=[codigo]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code


    #def obtener_detalle_prorroga(id_prorroga,estado,sucursal,credito,rut,considerada):
    #    """
    #    Servicio para obtener el detalle de prorroga
    #    """
    #
    #    package_name="PCK_PRORROGAS"
    #    procedure_name="RECUPERARPRORROGAS"
    #     
    #    if not id_prorroga:
    #        return "Faltan parámetros",400
    #    if not isinstance(id_prorroga,int):
    #        return "Parametro < idprorroga > tiene que ser un entero",400
    #
    #
    #
    #    params=[id_prorroga,estado,sucursal,credito,rut,considerada]
    #
    #    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
    #
    #    return response, status_code

    def obtener_detalle_cuota_posterior_prorroga(self,id_prorroga):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARCUOTASPOSTPRORROGA"
        params=[id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_detalle_cuota_anterior_prorroga(self,id_prorroga):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARCUOTASANTPRORROGA"
        params=[id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code


    def obtener_detalle_cargos_prorroga(self,id_prorroga):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARCARGOSPRORROGAS"
        params=[id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_detalle_rechazos_prorroga(self,id_prorroga):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARRECHAZOSPRORROGAS"
        params=[id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_cantidad_operaciones_prorrogas_por_rut(self,rut):
        package_name="PCK_PRORROGAS"
        procedure_name="CANTOPERACIONESPRORROGADASRUT"
        params={
            "P_RUT":rut
        }
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_number(procedure_name,package_name,params)
        return response, status_code

    def obtener_cantidad_operaciones_por_rut(self,rut):
        package_name="PCK_PRORROGAS"
        procedure_name="CANTOPERACIONESRUT"
        params={
            "P_RUT":rut
        }
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_number(procedure_name,package_name,params)
        return response, status_code

    def obtener_prorrogas_firmadas(self,id_usuario,id_prorroga):
        package_name="PCK_PRORROGAS"
        procedure_name="RECUPERARPRORROGASFIRMADAS"
        params=[id_usuario,id_prorroga]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_todas_prorrogas_firmadas(self):
        package_name="PCK_PRORROGAS"
        procedure_name="RECPRORROGASFIRMADASTODAS"
        response, status_code = self.funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)
        return response, status_code

    def obtener_prorrogas_firmas(self,id_usuario):
        package_name="PCK_PRORROGAS"
        procedure_name="RECPRORROGASFIRMAS"
        params=[id_usuario]
        #current_app.logger.info(params)
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_todas_prorrogas_firmas(self):
        package_name="PCK_PRORROGAS"
        procedure_name="RECPRORROGASFIRMASTODAS"
        response, status_code = self.funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)
        return response, status_code

    def validar_existencia_prorroga(self,operacion):
        package_name="PCK_PRORROGAS"
        procedure_name="EXISTEPRORROGA"
        params = [operacion]
        response, status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code


