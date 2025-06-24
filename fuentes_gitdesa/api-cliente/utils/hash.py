import hashlib
from flask import current_app

def get_clave_sha1(rut: str, str_value: str) -> str:
    """
    Genera un hash SHA-1 doble basado en el RUT y una cadena de entrada.
    Equivalente a la función `getClaveSHA1` en Kotlin.
    """
    
    try:
        if not isinstance(rut, str):
            rut = str(rut)
        if not isinstance(str_value, str):
            str_value = str(str_value)
 
        
        primer_hash = generar_hash(str_value + rut)
        
        if primer_hash is None:
            return ""
            
        segundo_hash = generar_hash(primer_hash)
        
        if segundo_hash is None:
            return ""
            
        resultado = segundo_hash.upper()
        return resultado
    except Exception as e:
        return ""

def generar_hash(text: str) -> str:
    """
    Genera un hash SHA-1 para una cadena de texto dada.
    Equivalente a la función `generarHash` en Kotlin.
    """
    
    try:
        # Codificar el texto en ISO-8859-1 (latin1)
        text_bytes = text.encode('ISO-8859-1')
        
        sha1_hash = hashlib.sha1(text_bytes).digest()
        
        resultado = get_hexadecimal(sha1_hash)
        return resultado
    except Exception as e:
        raise e

def get_hexadecimal(data: bytes) -> str:
    """
    Convierte un bytearray en su representación hexadecimal.
    Equivalente a la función `getHexadecimal` en Kotlin.
    """
    
    try:
        buf = []
        for b in data:
            # Convertir cada byte a su representación hexadecimal
            half_byte_1 = (b >> 4) & 0x0F
            half_byte_2 = b & 0x0F
            buf.append(hex_digit(half_byte_1))
            buf.append(hex_digit(half_byte_2))
        
        resultado = ''.join(buf)
        return resultado
    except Exception as e:
        raise e

def hex_digit(value: int) -> str:
    """
    Convierte un valor entre 0 y 15 a su carácter hexadecimal correspondiente.
    """
    try:
        if 0 <= value <= 9:
            return chr(ord('0') + value)
        elif 10 <= value <= 15:
            return chr(ord('a') + (value - 10))
        else:
            error_msg = f"Valor fuera del rango hexadecimal (0-15): {value}"
            raise ValueError(error_msg)
    except Exception as e:
        raise e

def verificar_password(password: str, hash_password: str, rut: str) -> bool:
    """
    Verifica si la contraseña ingresada coincide con la contraseña de la tabla claveinternet
    """
    
    try:
        # Validar que los datos de entrada no sean None
        if password is None or hash_password is None or rut is None:
            return False
            
        # Validar que hash_password no esté vacío
        if not hash_password:
            return False
            
        hash_generado = get_clave_sha1(rut, password)
        
        resultado = hash_generado == hash_password.upper()
        return resultado
    except Exception as e:
        return False
