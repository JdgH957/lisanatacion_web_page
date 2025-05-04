from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Annotated
from api.schemas.club import ClubOut 

# ✅ Esquema base
class EntrenadorBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    fecha_asig: date
    club_actual: str | None = None
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int

# ✅ Crear entrenador
class EntrenadorCreate(EntrenadorBase):
    pass  # No hay campos adicionales

# ✅ Actualizar entrenador
class EntrenadorUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    email: EmailStr | None = None
    fecha_asig: date | None = None
    club_actual: str | None = None
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int | None = None


class EntrenadorOut(EntrenadorBase):
    id: int
    club: ClubOut | None = None  # Relación con el club

    class Config:
        orm_mode = True