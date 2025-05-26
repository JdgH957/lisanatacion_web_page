# app/application/DTOS/miembro_dto.py

from pydantic import BaseModel
from typing import Optional

class MiembroCreateDTO(BaseModel):
    nombre: str
    edad: int
    curso_id: int
    tipo_miembro: str
    estado_pago: str

class MiembroUpdateDTO(BaseModel):
    nombre: Optional[str]
    edad: Optional[int]
    curso_id: Optional[int]
    tipo_miembro: Optional[str]
    estado_pago: Optional[str]

class MiembroOutDTO(BaseModel):
    id_miembro: int
    nombre: str
    edad: int
    curso_id: int
    tipo_miembro: str
    estado_pago: str

    class Config:
        from_attributes = True


class InscripcionMiembroRequest(BaseModel):
    nombre: str
    edad: int
    curso_id: int
    tipo_miembro: str  # "prueba" o "mensual"
