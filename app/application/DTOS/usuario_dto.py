from pydantic import BaseModel
from enum import Enum
from datetime import date

class RolUsuarioEnum(str, Enum):
    ENTRENADOR = "entrenador"
    CLUB = "club"

class UsuarioCreateDTO(BaseModel):
    nombre: str
    apellido: str
    email: str
    contra: str
    fecha_asig: date
    rol: RolUsuarioEnum
    contacto: str
    edad: int

class UsuarioOutDTO(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    rol: str
    class Config:
        orm_mode = True
