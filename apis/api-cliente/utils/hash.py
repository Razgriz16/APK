import hashlib

def get_clave_sha1(rut: str, str_value: str) -> str:
    """
    Genera un hash SHA-1 doble basado en el RUT y una cadena de entrada.
    Equivalente a la función `getClaveSHA1` en Kotlin.
    """
    primer_hash = generar_hash(str_value + rut)
    segundo_hash = generar_hash(primer_hash)
    return segundo_hash.upper()

def generar_hash(text: str) -> str:
    """
    Genera un hash SHA-1 para una cadena de texto dada.
    Equivalente a la función `generarHash` en Kotlin.
    """
    try:
        # Codificar el texto en ISO-8859-1 (latin1)
        text_bytes = text.encode('ISO-8859-1')
        sha1_hash = hashlib.sha1(text_bytes).digest()
        return get_hexadecimal(sha1_hash)
    except Exception as e:
        print(f"Error al generar el hash: {e}")
        return None

def get_hexadecimal(data: bytes) -> str:
    """
    Convierte un bytearray en su representación hexadecimal.
    Equivalente a la función `getHexadecimal` en Kotlin.
    """
    buf = []
    for b in data:
        # Convertir cada byte a su representación hexadecimal
        half_byte_1 = (b >> 4) & 0x0F
        half_byte_2 = b & 0x0F
        buf.append(hex_digit(half_byte_1))
        buf.append(hex_digit(half_byte_2))
    return ''.join(buf)

def hex_digit(value: int) -> str:
    """
    Convierte un valor entre 0 y 15 a su carácter hexadecimal correspondiente.
    """
    if 0 <= value <= 9:
        return chr(ord('0') + value)
    elif 10 <= value <= 15:
        return chr(ord('a') + (value - 10))
    else:
        raise ValueError("Valor fuera del rango hexadecimal (0-15)")

def verificar_password(password: str, hash_password: str, rut: str) -> bool:
    """
    Verifica si la contraseña ingresada coincide con la contraseña de la tabla claveinternet
    """
    hash_generado = get_clave_sha1(rut, password)
    return hash_generado == hash_password.upper()
