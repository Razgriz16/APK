from flask import current_app
import traceback

class DapRepository():
    def __init__(self, funciones_db):
        self.funciones_db = funciones_db

    def recuperar_operaciones(self, rut_cliente, estado, fecha_inicio, fecha_fin, indicador1, indicador2):
        try:
            package_name = "DEPOSITO.PCK_DEPOSITO"
            procedure_name = "DepRecOpsActCli"
            params = [rut_cliente, estado, fecha_inicio, fecha_fin, indicador1, indicador2]
            response, status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)
            current_app.logger.info(f"Response: {response}")
            current_app.logger.info(f"Status code: {status_code}")
            return response, status_code
        except Exception as e:
            current_app.logger.error(f"Error in obtener_cuenta_ahorro: {str(e)}")
            current_app.logger.error(traceback.format_exc())
            return None, 500
    
