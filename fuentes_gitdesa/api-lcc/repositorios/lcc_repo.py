class LccRepository():
    """
    Repositorios para operaciones de datos relacionadas con lcc
    """
    def __init__(self,funciones_db):
        self.funciones_db=funciones_db

    def get_lineacc(self,rut):
        package_name="LINEACC.PCK_LINEACC"
        procedure_name="RECLINEACC"
        params = [rut]
        response , status_code = self.funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)
        return response, status_code
