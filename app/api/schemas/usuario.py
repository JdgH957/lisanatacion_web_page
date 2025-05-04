from pydantic import BaseModel, EmailStr, constr
from datetime import date
from app.models.usuarios import RolUsuarioEnum
from typing import Annotated 

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    fecha_asig: date
    rol: RolUsuarioEnum
    contacto:int
    edad:int


class UsuarioCreate(UsuarioBase):
    contra: Annotated[str, constr(min_length=8, max_length=50)] 


class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    email: EmailStr | None = None
    fecha_asig: date | None = None
    rol: RolUsuarioEnum | None = None
    contra: Annotated[str, constr(min_length=8, max_length=50)] | None = None
    contacto:int
    edad:int



# ✅ Esquema de respuesta (opcional)
class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
