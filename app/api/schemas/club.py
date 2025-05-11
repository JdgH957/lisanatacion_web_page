from __future__ import annotations
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .entrenador import EntrenadorOut

# ✅ Esquema base
class ClubBase(BaseModel):
    nombre_club: str
    fecha_creacion: date
    lider_id: int
    email: EmailStr
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int

# ✅ Crear entrenador
class ClubCreate(ClubBase):
    pass  # No hay campos adicionales

# ✅ Actualizar entrenador
class ClubUpdate(BaseModel):
    nombre_club: str
    fecha_creacion: date
    lider_id: int
    email: EmailStr
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int

class ClubOut(ClubBase):
    id: int
    lider: EntrenadorOut | None = None  # Relación con líder
    entrenadores: List[EntrenadorOut] = []  # Lista de entrenadores

    class Config:
        orm_mode = True
