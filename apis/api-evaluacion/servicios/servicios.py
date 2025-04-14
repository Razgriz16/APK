import funciones_db
from flask import abort, render_template, current_app

def obtener_credito(credito,rut,estado=-1,prorrogados='N'):
    """
    Servicio para obtener credito a partir de rut y/o credito
    """
    package_name="PCK_CREDITO"
    procedure_name="RECUPERACREDITOS"

    if not credito and not rut:
        return "Faltan parámetros",400

    if credito == -1 and rut == -1:
        return "Faltan parámetros",400

    if prorrogados not in ['S','N']:
        return {"error": "El parámetro para 'prorrogados' debe ser 'S' o 'N'"}, 400

    params = [credito,estado,rut,prorrogados]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code


def obtener_credito_bloqueo(operacion,estado='0',judicial='0'):
    """
    Servicio para obtener credito a partir de rut y/o credito
    """
    package_name="PCK_CREDITO"
    procedure_name="CRCRECBLOQUEOS"

    #estado [A,D,0] ?
    
    if not isinstance(operacion,int):
        return "Parametro < operacion > tiene que ser un entero",400

    if not operacion:
        return "Faltan parámetros",400

    params = [operacion,estado,judicial]

    current_app.logger.info(params)
    
    response , status_code = funciones_db.pkg_exe_par_cursor(procedure_name,package_name,params)

    return response, status_code


def obtener_cuotas(operacion,peso='N'):
    """
    Servicio para obtener cuotas
    """
    package_name="PCK_CREDITO"
    procedure_name="RECUPERARCUOTAS"
    collection_type_name="CREDITO.CRC_CUOTAS_CREDITO_TAB"

    if not operacion:
        return "Faltan parámetros",400

    if not isinstance(operacion,int):
        return "Parametro < operacion > tiene que ser un entero",400

    if peso not in ['S','N']:
        return {"error": "El parámetro para 'prorrogados' debe ser 'S' o 'N'"}, 400



    params = {
        "P_OPERACION":operacion,
        "P_PESO":peso,
    }

    current_app.logger.info(params)
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_collection(procedure_name,package_name,params,collection_type_name)



    return response, status_code

def obtener_movimientos(credito):
    """
    Servicio para obtener los moviemientos
    """
    package_name="PCK_CREDITO"
    procedure_name="RECUPERARMOVIMIENTOS"

    if not credito:
        return "Faltan parámetros",400
    if not isinstance(credito,int):
        return "Parametro < credito > tiene que ser un entero",400

    params = [credito]




    current_app.logger.info(params)
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code



def obtener_operaciones_cliente(todos,fecha,cliente=0,operacion=0):
    """
    Servicio para obtener operaciones de clientes
    """
    package_name="CARTERAVENCIDA.PCK_CVENCIDA"
    procedure_name="CVERECOPERACIONESCLIENTE"
    collection_type_name="CARTERAVENCIDA.CVE_OPERACIONES_TAB"

    if not operacion:
        return "Faltan parámetros",400

    params = {
        "P_CLIENTE":cliente,
        "P_OPERACION":operacion,
        "P_TODOS":todos,
        "P_FECHAPROCESO":fecha,
    }

    current_app.logger.info(params)
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_collection(procedure_name,package_name,params,collection_type_name)

    return response, status_code

################################################
## PRORROGA - Queries de DataConDAO.java   #####
################################################
def obtener_detalle_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de prorroga
    """
    package_name="PCK_CREDITO"
    procedure_name="RECPRORROGA"

    if not id_prorroga:
        return "Faltan parámetros",400
    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener rechazos prorroga
    """
    package_name="PCK_CREDITO"
    procedure_name="RECRECHAZOSPRORROGA"

    if not id_prorroga:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code


def obtener_cuotas_prorrogas(id_prorroga,cuota_desde,cuota_hasta):
    """
    Servicio para obtener cuotas prorrogas 
    """
    package_name="PCK_CREDITO"
    procedure_name="RECCUOTASPRORROGA"

    if not id_prorroga or not cuota_desde or not cuota_hasta:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga,cuota_desde,cuota_hasta]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener rechazos prorroga posterior
    """
    package_name="PCK_CREDITO"
    procedure_name="RECCUOTASPOSTPRORROGA"

    if not id_prorroga:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_detalle_cuotas_prorrogas_posterior(id_prorroga):
    """
    Servicio para obtener rechazos prorroga posterior
    """
    package_name="PCK_CREDITO"
    procedure_name="RECDETALLECUOTAPOSTPRORROGA"

    if not id_prorroga:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener los cargos de prorroga
    """
    package_name="PCK_CREDITO"
    procedure_name="RECCARGOSPRORROGA"

    if not id_prorroga:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params = [id_prorroga]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_creditos_prorroga(rut):
    """
    Servicio para obtener credito prorroga
    """

    package_name="PCK_CREDITO"
    procedure_name="RECCREDITOSPRORROGA"

    if not rut:
        return "Faltan parámetros",400
    if not isinstance(rut,int):
        return "Parametro < rut > tiene que ser un entero",400

    params = [rut]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_rechazo_prorroga_usuario(id_prorroga,id_usuario):
    """
    Servicio para obtener rechazo prorroga
    """

    package_name="PCK_CREDITO"
    procedure_name="RECRECHAZOUSUARIO"

    if not id_prorroga or not id_usuario:
        return "Faltan parámetros",400

    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400
    if not isinstance(id_usuario,int):
        return "Parametro < idusuario > tiene que ser un entero",400

    params = [id_prorroga,id_usuario]
    current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_linea_credito(rut):
    """
    Servicio para obtener linea credito
    """

    package_name="PCK_CREDITO"
    procedure_name="RECLINEACC"

    if not rut:
        return "Faltan parámetros",400
    if not isinstance(rut,int):
        return "Parametro < idusuario > tiene que ser un entero",400

    params = [rut]
    #current_app.logger.info(params) #Log de params
    
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

#####################################
def obtener_parametros():
    """
    Servicio para obtener parametros
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARPARAMETROS"

    response , status_code = funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)

    return response, status_code

def obtener_grupo_prorrogas(codigo):
    """
    Servicio para obtener parametros de grupos de prorroga 
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARPARAMETROSGRUPO"
     
    if not codigo:
        return "Faltan parámetros",400

    if not isinstance(codigo,int):
        return "Parametro < idprorroga > tiene que ser un entero",400



    params=[codigo]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

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

def obtener_detalle_cuota_posterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cutoas posterior de la prorroga
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARCUOTASPOSTPRORROGA"
     
    if not id_prorroga:
        return "Faltan parámetros",400
    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400


    params=[id_prorroga]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_detalle_cuota_anterior_prorroga(id_prorroga):
    """
    Servicio para obtener detalle de cutoas anterior de la prorroga
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARCUOTASANTPRORROGA"
     
    if not id_prorroga:
        return "Faltan parámetros",400
    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400

    params=[id_prorroga]
    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code


def obtener_detalle_cargos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de cargos de prorroga
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARCARGOSPRORROGAS"
     
    if not id_prorroga:
        return "Faltan parámetros",400
    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400


    params=[id_prorroga]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_detalle_rechazos_prorroga(id_prorroga):
    """
    Servicio para obtener el detalle de rechazos de prorrogas
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARRECHAZOSPRORROGAS"
     
    if not id_prorroga:
        return "Faltan parámetros",400
    if not isinstance(id_prorroga,int):
        return "Parametro < idprorroga > tiene que ser un entero",400


    params=[id_prorroga]

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code



def obtener_cantidad_operaciones_prorrogas_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones prorrogadas por rut
    """

    package_name="PCK_PRORROGAS"
    procedure_name="CANTOPERACIONESPRORROGADASRUT"
     
    if not rut:
        return "Faltan parámetros",400
    if not isinstance(rut,int):
        return "Parametro < rut > tiene que ser un entero",400


    params={
        "P_RUT":rut
    }

    response , status_code = funciones_db.pkg_exe_par_error_msg_number(procedure_name,package_name,params)

    return response, status_code


def obtener_cantidad_operaciones_por_rut(rut):
    """
    Servicio para obtener la cantidad de operaciones por rut
    """

    package_name="PCK_PRORROGAS"
    procedure_name="CANTOPERACIONESRUT"
     
    if not rut:
        return "Faltan parámetros",400
    if not isinstance(rut,int):
        return "Parametro < rut > tiene que ser un entero",400

    params={
        "P_RUT":rut
    }

    response , status_code = funciones_db.pkg_exe_par_error_msg_number(procedure_name,package_name,params)

    return response, status_code


def obtener_prorrogas_firmadas(id_usuario,id_prorroga):
    """
    Servicio para obtener las prorrogas firmadas
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECUPERARPRORROGASFIRMADAS"
     
    if not id_usuario:
        return "Faltan parámetros",400
    if not isinstance(id_usuario,int):
        return "Parametro < idusuario > tiene que ser un entero",400
    if id_prorroga != -1:
        if not isinstance(id_prorroga,int):
    	    return "Parametro < idprorroga > tiene que ser un entero",400

    params=[id_usuario,id_prorroga]
    current_app.logger.info(params)
    

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_todas_prorrogas_firmadas():
    """
    Servicio para obtener todas las prorrogas firmadas
    """
    
    package_name="PCK_PRORROGAS"
    procedure_name="RECPRORROGASFIRMADASTODAS"
   

    response, status_code = funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)
    return response, status_code

def obtener_prorrogas_firmas(id_usuario):
    """
    Servicio para obtener las prorrogas firmas
    """

    package_name="PCK_PRORROGAS"
    procedure_name="RECPRORROGASFIRMAS"
     
    if not id_usuario:
        return "Faltan parámetros",400
    if not isinstance(id_usuario,int):
        return "Parametro < idusuario > tiene que ser un entero",400

    params=[id_usuario]
    current_app.logger.info(params)
    

    response , status_code = funciones_db.pkg_exe_par_error_msg_cursor(procedure_name,package_name,params)

    return response, status_code

def obtener_todas_prorrogas_firmas():
    """
    Servicio para obtener todas las prorrogas firmas
    """
    
    package_name="PCK_PRORROGAS"
    procedure_name="RECPRORROGASFIRMASTODAS"
   

    response, status_code = funciones_db.pkg_exe_error_msg_cursor(procedure_name,package_name)
    return response, status_code
