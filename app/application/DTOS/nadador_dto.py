from typing import List, Optional
from pydantic import BaseModel, EmailStr
from app.application.common.enums import Disciplinas, Categorias
from app.application.DTOS.nadador_dto import NadadorOutDTO  # Asegúrate de tener este DTO bien definido

class NadadorCreateDTO(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    contra: str
    fecha_asig: str
    rol: str
    edad: int
    peso: float
    categorias: list[Disciplinas]
    disciplinas: list[Categorias]
    id_entrenador: Optional[int]
    id_club: Optional[int]
    imagen: Optional[str] = None  # si es una URL o ruta de imagen

class NadadorUpdateDTO(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    contra: Optional[str]
    fecha_asig: Optional[str]
    rol: Optional[str]
    edad: Optional[int]
    peso: Optional[float]
    categorias: Optional[List[Disciplinas]]
    disciplinas: Optional[List[Categorias]]
    id_entrenador: Optional[int]
    id_club: Optional[int]
    imagen: Optional[str]

class NadadorOutDTO(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    fecha_asig: str
    rol: str
    categorias: List[Disciplinas]
    disciplinas: List[Categorias]
    imagen: Optional[str]

    class Config:
        orm_mode = True