from typing import Optional
from pydantic import BaseModel


class ClubCreateDTO(BaseModel):
    nombre: str
    descripcion: str
    email: str
    fecha_fundacion: str
    pais: str
    ciudad: str
    imagen: Optional[str] = None  # si es una URL o ruta de imagen


class ClubUpdateDTO(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    email: Optional[str]
    fecha_fundacion: Optional[str]
    pais: Optional[str]
    ciudad: Optional[str]
    imagen: Optional[str]  # si es una URL o ruta de imagen

class ClubOutDTO(BaseModel):
    nombre: str
    descripcion: str
    email: Optional[str] = None
    imagen: Optional[str] = None  # si es una URL o ruta de imagen

    class Config:
        orm_mode = True