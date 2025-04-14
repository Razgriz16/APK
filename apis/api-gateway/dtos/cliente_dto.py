from pydantic import BaseModel

class LoginDto(BaseModel):
    rut: str
    clave: str
