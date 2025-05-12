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
    email: EmailStr
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int
    entrenadores_ids: List[int]  # al menos uno

# ✅ Crear entrenador
class ClubCreate(ClubBase):
    pass  # No hay campos adicionales

# ✅ Actualizar entrenador
class ClubUpdate(BaseModel):
    nombre_club: str
    fecha_creacion: date
    email: EmailStr
    titulos: str | None = None
    experiencia: str | None = None
    años_exp: int
    entrenadores_ids: List[int]

class ClubOut(ClubBase):
    id: int
    entrenadores: List[EntrenadorOut] = []  # Lista de entrenadores

    class Config:
        orm_mode = True
