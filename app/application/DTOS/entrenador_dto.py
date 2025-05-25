from typing import List, Optional
from pydantic import BaseModel, EmailStr
from app.application.common.enums import Disciplinas, Categorias
from app.application.DTOS.nadador_dto import NadadorOutDTO  # Asegúrate de tener este DTO bien definido


class EntrenadorCreateDTO(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    contacto: str
    edad: int
    disciplinas: List[Disciplinas]
    categorias: List[Categorias]
    id_club: int
    experiencia: str
    imagen: Optional[str] = None  # si es una URL o ruta de imagen


class EntrenadorUpdateDTO(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    contacto: Optional[str]
    edad: Optional[int]
    disciplinas: Optional[List[Disciplinas]]
    categorias: Optional[List[Categorias]]
    id_club: Optional[int]
    experiencia: Optional[str]
    imagen: Optional[str]


class EntrenadorOutDTO(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    disciplinas: List[str]
    categorias: List[str]
    experiencia: str
    imagen: Optional[str]
    nadadores: List[NadadorOutDTO]

    class Config:
        orm_mode = True
