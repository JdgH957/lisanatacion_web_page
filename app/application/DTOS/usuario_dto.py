from typing import Optional
from pydantic import BaseModel, EmailStr
from app.application.common.enums import RolUsuario
from datetime import date

class UsuarioCreateDTO(BaseModel):
    nombre: str
    apellido: str
    email: str
    contra: str
    fecha_asig: date
    rol: RolUsuario
    contacto: str
    edad: int

class UsuarioUpdateDTO(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    contra: Optional[str] = None
    fecha_asig: Optional[date] = None
    rol: Optional[str] = None
    contacto: Optional[str] = None
    edad: Optional[int] = None
    
class UsuarioOutDTO(BaseModel):
    nombre: str
    apellido: str
    email: str
    rol: RolUsuario
    class Config:
        orm_mode = True
