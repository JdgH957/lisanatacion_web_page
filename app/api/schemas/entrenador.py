from __future__ import annotations
from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional
from .club import ClubOut
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .club import ClubOut  # Solo para validación de tipos, no se ejecuta


# ✅ Esquema base
class EntrenadorBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    fecha_asig: date
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int
    club_id: int  

# ✅ Crear entrenador
class EntrenadorCreate(EntrenadorBase):
    pass  # No hay campos adicionales

# ✅ Actualizar entrenador
class EntrenadorUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    email: EmailStr | None = None
    fecha_asig: date | None = None
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int | None = None
    club_id: int 

class EntrenadorOut(EntrenadorBase):
    id: int
    club: ClubOut | None = None  # Relación con el club

    class Config:
        orm_mode = True