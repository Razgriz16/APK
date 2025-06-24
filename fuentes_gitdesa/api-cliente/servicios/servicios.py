from utils.jwt_utils import JWTManager
from utils.hash import verificar_password
from utils.respuesta_util import procesar_respuesta_plsql
from repositorios import cliente_repo as rp
from utils.error_util import handle_service_error
from flask import g, current_app
import funciones_db


repo = rp.ClienteRepository(funciones_db)

def login(rut, clave):
    """
    Servicio iniciar sesion
    Args:
        rut: int
        clave: str
    Return: Si las credenciales son validas retorna access y refresh token
    """

    if not rut or not clave:
        return {"error_code": 400, "error_message": "Faltan parámetros", "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Validar que existe un cliente con el rut que se paso
        int_rut = int(rut)
        response, status_code = repo.obtener_rut_clave_usuario_por_rut(int_rut)
        current_app.logger.info(response)
        processed_response, processed_status_code = procesar_respuesta_plsql(response,status_code,f"Auth de usuario {rut}")
        current_app.logger.info(processed_response)
        if processed_status_code != 200:
            return processed_response, processed_status_code

        # Comparar passwords
        data = processed_response.get("data",[])
        if not data:
            return {"error_code": 400, "error_message": "Credenciales incorrectas", 
                    "trace_id": g.trace_id, "data": []}, 400

        cliente_data = data[0]
        clave_hasheada = cliente_data.get("clave")
        if not verificar_password(clave,clave_hasheada,rut):
            return {"error_code": 401, "error_message": "Credenciales incorrectas", 
                    "trace_id": g.trace_id, "data": []}, 401

        # Crear accessToken
        jwt_manager = JWTManager()
        access_token = jwt_manager.generar_access_token(rut)
        refresh_token = jwt_manager.generar_refresh_token(rut)

        # Si tiene refreshToken eliminarlo
        # TODO
        # Guardar refreshToken en BD
        # TODO

        # return access y refreshToken
        res = {
            "error_code": 0,
            "error_message": "",
            "trace_id": g.trace_id,
            "data": [{
                "access_token": access_token,
                "refresh_token": refresh_token,
                "usuario": {
                    "rut": rut,
                    "nombre": cliente_data.get("nombre", ""),
                }
            }]
        }
        return res, 200
    except Exception as e:
        return handle_service_error(e,context=f"Login de usuario con RUT <{rut}>")


def get_usuario_por_rut(rut):
    """
    Servicio obtener informacion del cliente
    Args:
        rut: int
    Return: Si el rut es valido retorna informacion del cliente
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El rut debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener datos del cliente por RUT
        response, status_code = repo.obtener_cliente(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener información de cliente con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener información de cliente con RUT {rut}")

def get_direccion_cliente(rut):
    """
    Servicio para obtener la dirección del cliente por RUT.
    Args:
        rut: int
    Return: Dirección del cliente si el RUT es válido.
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El RUT debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener dirección del cliente por RUT
        response, status_code = repo.obtener_direccion_por_rut(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener dirección de cliente con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener dirección de cliente con RUT {rut}")

def get_telefono_cliente(rut):
    """
    Servicio para obtener el teléfono del cliente por RUT.
    Args:
        rut: int
    Return: Teléfono del cliente si el RUT es válido.
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El RUT debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener teléfono del cliente por RUT
        response, status_code = repo.obtener_telefono_por_rut(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener teléfono de cliente con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener teléfono de cliente con RUT {rut}")

def get_telefono_verificado_cliente(rut):
    """
    Servicio para obtener el teléfono verificado del cliente por RUT.
    Args:
        rut: int
    Return: Teléfono verificado del cliente si el RUT es válido.
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El RUT debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener teléfono verificado del cliente por RUT
        response, status_code = repo.obtener_telefono_verificado_por_rut(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener teléfono verificado de cliente con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener teléfono verificado de cliente con RUT {rut}")

def get_correo_cliente(rut):
    """
    Servicio para obtener el correo del cliente por RUT.
    Args:
        rut: int
    Return: Correo del cliente si el RUT es válido.
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El RUT debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener correo del cliente por RUT
        response, status_code = repo.obtener_correo_por_rut(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener correo de cliente con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener correo de cliente con RUT {rut}")

def get_sucursal_funcionario(rut):
    """
    Servicio para obtener la sucursal del funcionario por RUT.
    Args:
        rut: int
    Return: Sucursal del funcionario si el RUT es válido.
    """
    # Validación de parámetros
    if not rut:
        return {"error_code": 400, "error_message": "Rut es requerido", "trace_id": g.trace_id, "data": []}, 400
    
    if not isinstance(rut, int):
        return {"error_code": 400, "error_message": "El RUT debe ser un número entero", 
                "trace_id": g.trace_id, "data": []}, 400
    
    try:
        # Obtener sucursal del funcionario por RUT
        response, status_code = repo.obtener_sucursal_funcionario(rut)
        
        # Procesar respuesta para manejar errores de BD
        return procesar_respuesta_plsql(
            response, 
            status_code, 
            f"Obtener sucursal de funcionario con RUT {rut}"
        )
    except Exception as e:
        return handle_service_error(e, context=f"Obtener sucursal de funcionario con RUT {rut}")
