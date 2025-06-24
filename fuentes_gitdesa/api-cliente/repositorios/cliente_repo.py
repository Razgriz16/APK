class ClienteRepository():
    """
    Repositorio para operaciones de datos realacionada con cientes
    """
    def __init__(self,funciones_db):
        self.funciones_db=funciones_db
    def obtener_cliente(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="CliRecCliente"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_rut_clave_usuario_por_rut(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="CLIRECRUTPASSWORD"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_direccion_por_rut(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="CLIRECDIRECCION"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code


    def obtener_telefono_por_rut(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="CLIRECTELEFONO"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code

    def obtener_telefono_verificado_por_rut(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="cliRecTelefono_Verificado"
        params = {
            "P_RUT":rut
        }
        response , status_code = self.funciones_db.pkg_exe_par_string(procedure_name,package_name,params)
        return response, status_code


    def obtener_correo_por_rut(self,rut):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="obtenerCorreoPorRut"
        params = {
            "P_RUT":rut
        }
        response , status_code = self.funciones_db.pkg_exe_par_string(procedure_name,package_name,params)
        return response, status_code

    def obtener_sucursal_funcionario(self,usuario):
        package_name="CLIENTE.PCK_CLIENTE"
        procedure_name="RecuperarSucursalFuncionario"
        params = {
            "P_usuario":usuario
        }
        response , status_code = self.funciones_db.pkg_exe_par_string(procedure_name,package_name,params)
        return response, status_code

