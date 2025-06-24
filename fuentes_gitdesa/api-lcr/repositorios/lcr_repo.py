class LcrRepository():
    """
    Repositorios para operaciones de datos relacionadas con lcc
    """
    def __init__(self,funciones_db):
        self.funciones_db=funciones_db

    def get_lineacr(self,rut):
        package_name="LINEACRD.PCK_LCR"
        procedure_name="RECLCRCLIENTE"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code

    def get_mov_lineacr(self, nro_cuenta, cantidad):
        package_name="LINEACRD.PCK_LCR"
        procedure_name="RECMOVLCRCLIENTE"
        params = [nro_cuenta, cantidad]
        response , status_code = self.funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)
        return response, status_code
