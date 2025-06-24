class BaseRepository:
    """
    Base class for repositories that interact with PL/SQL procedures.
    """
    def __init__(self, db_functions):
        """
        Initializes the repository with database functions.
        
        Args:
            db_functions: Object with methods to interact with the database.
        """
        self.db_functions = db_functions
    
    def ejecutar_procedure(self, package_name, procedure_name, params=None):
        """
        Executes a PL/SQL procedure with parameters and returns cursor data.
        
        Args:
            package_name (str): PL/SQL package name.
            procedure_name (str): Procedure name.
            params (list, optional): List of parameters for the procedure.
            
        Returns:
            tuple: (response, status_code) where response is the raw response
                  and status_code is the status code.
        """
        if params is None:
            return self.db_functions.pkg_exe_error_msg_cursor(
                procedure_name, package_name, []
            )
        else:
            return self.db_functions.pkg_exe_par_error_msg_cursor(
                procedure_name, package_name, params
            )
    
    def ejecutar_procedure_simple(self, package_name, procedure_name, params=None):
        """
        Executes a PL/SQL procedure that returns only a cursor without error handling parameters.
        
        Args:
            package_name (str): PL/SQL package name.
            procedure_name (str): Procedure name.
            params (list, optional): List of parameters for the procedure.
            
        Returns:
            tuple: (response, status_code)
        """
        if params is None:
            return self.db_functions.pkg_exe_no_params_cursor(
                procedure_name, package_name
            )
        else:
            return self.db_functions.pkg_exe_par_cursor(
                procedure_name, package_name, params
            )
    
    def ejecutar_collection_procedure(self, package_name, procedure_name, params, collection_type_name):
        """
        Executes a PL/SQL procedure that returns a collection.
        
        Args:
            package_name (str): PL/SQL package name.
            procedure_name (str): Procedure name.
            params (dict): Dictionary of parameters for the procedure.
            collection_type_name (str): The name of the collection type.
            
        Returns:
            tuple: (response, status_code)
        """
        return self.db_functions.pkg_exe_par_error_msg_collection(
            procedure_name, package_name, params, collection_type_name
        )
