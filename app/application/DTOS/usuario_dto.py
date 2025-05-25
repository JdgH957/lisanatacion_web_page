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
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    contra: Optional[str]
    fecha_asig: Optional[date]
    rol: Optional[RolUsuario]
    contacto: Optional[str]
    edad: Optional[int]

class UsuarioOutDTO(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: str
    rol: RolUsuario
    class Config:
        orm_mode = True
