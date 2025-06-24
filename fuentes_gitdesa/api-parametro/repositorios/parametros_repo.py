class ParametrosRepository():
    """
    Repositorio para operaciones de datos relacionadas con parametros
    """
    def __init__(self,funciones_db):
        self.funciones_db=funciones_db
    
    def recuperar_sucursales_activas(self):
        package_name = "SGT.PCK_SGT"  
        procedure_name = "SGTRECSUCURSALES"
        params = []
        response, status_code = self.funciones_db.pkg_exe_no_params_cursor(procedure_name, package_name)
        return response, status_code

    def obtener_sucursal(self,codigo):
        package_name = "SGT.PCK_SGT"
        procedure_name = "obtener_sucursal"
        params = [codigo]
        response, status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)
        return response, status_code

    def obtener_comunas(self,comuna,ciudad):
        package_name = "SGT.PCK_SGT"
        procedure_name = "SGTRECCOMUNAS"
        params = [comuna,ciudad]
        response, status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name, package_name, params)
        return response, status_code

    def obtener_ciudades(self,ciudad):
        package_name = "SGT.PCK_SGT"
        procedure_name = "SGTRECCIUDADES" 
        params = [ciudad]
        response, status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name, package_name, params)
        return response, status_code

    def obtener_parametros(self):
        package_name = "SGT.PCK_SGT"
        procedure_name = "SGTRECPARAMETRO"
        params = []
        response, status_code = self.funciones_db.pkg_exe_error_msg_cursor(procedure_name, package_name,params)
        return response, status_code

    def obtener_credito_bloqueo(self,operacion,estado,judicial):
        package_name = "PCK_CREDITO"
        procedure_name = "CRCRECBLOQUEOSs"
        params = [operacion,estado,judicial]
        response, status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name, package_name,params)
        return response, status_code

    def obtener_cliente(self,rut):
        package_name = "CLIENTE.PCK_CLIENTE"
        procedure_name = "CliRecCliente"
        params = [rut]
        response, status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name, package_name,params)
        return response, status_code


