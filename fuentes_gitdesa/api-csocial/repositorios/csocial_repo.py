from flask import current_app
import traceback

class CsocialRepository():
    def __init__(self, funciones_db):
        self.funciones_db = funciones_db
        
    def obtener_cuenta_csocial(self, rut_titular):
        try:
            package_name = "CSOCIAL.PCKCSOCIAL"
            procedure_name = "RECCUENTACSOCIAL"
            params = [rut_titular]
            response, status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name, package_name, params)
            current_app.logger.info(f"Response: {response}")
            current_app.logger.info(f"Status code: {status_code}")
            return response, status_code
        except Exception as e:
            current_app.logger.error(f"Error in obtener_cuenta_ahorro: {str(e)}")
            current_app.logger.error(traceback.format_exc())
            return None, 500

    def obtener_ultimos_movimientos(self, cuenta,cantidad):
        try:
            package_name = "CSOCIAL.PCKCSOCIAL"
            procedure_name = "RECULTIMOSMOVIMIENTOS"
            params = [cuenta,cantidad]
            response, status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
            current_app.logger.info(f"Response: {response}")
            current_app.logger.info(f"Status code: {status_code}")
            return response, status_code
        except Exception as e:
            current_app.logger.error(f"Error in obtener_movimientos: {str(e)}")
            current_app.logger.error(traceback.format_exc())
            return None, 500

    
#    def verificar_existencia_bloqueo(self, rut):
#        try:
#            package_name = "AHORRO.PCK_AHORRO"
#            procedure_name = "BloqDBFUAF_Final"
#            params = {
#                "P_RUT": rut
#            }
#            response, status_code = self.funciones_db.pkg_exe_par_number(procedure_name, package_name, params)
#            return response, status_code
#        except Exception as e:
#            current_app.logger.error(f"Error in verificar_existencia_bloqueo: {str(e)}")
#            current_app.logger.error(traceback.format_exc())
#            return None, 500
#


  # PROCEDURE RECUPERARMOVIMIENTOSFECHA(
  #     P_NUMERO_CUENTA         IN   AHORRO.CUENTAAHORRO.NUMEROCUENTA%TYPE,
  #     P_FECHA_INICIO          IN   VARCHAR2,
  #     P_FECHA_FIN             IN   VARCHAR2,
  #     P_ERROR                 OUT  NUMBER,
  #     P_MSG_ERROR             OUT  VARCHAR2,
  #     P_MOVIMIENTOS           OUT  SYS_REFCURSOR
  # );
  #  PROCEDURE RECUPERARULTIMOSMOVIMIENTOS (
  #  P_NUMERO_CUENTA         IN   AHORRO.CUENTAAHORRO.NUMEROCUENTA%TYPE,
  #  P_CANTIDAD              IN   NUMBER,
  #  P_ERROR                 OUT  NUMBER,
  #  P_MSG_ERROR             OUT  VARCHAR2,
  #  P_MOVIMIENTOS           OUT  SYS_REFCURSOR
  #  );
