from __future__ import annotations
from typing import Optional, List

from app.Domain.models.entrenador import Entrenador
from app.Domain.models.nadador import Nadador

class Club:
    def __init__(
        self,
        nombre: str,
        descripcion: str,
        email: str,
        fecha_fundacion: str,
        pais: str,
        ciudad: str,
        imagen: Optional[str] = None,
        entrenadores: Optional[List[Entrenador]] = None,
        nadadores: Optional[List[Nadador]] = None
    ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.email = email
        self.fecha_fundacion = fecha_fundacion
        self.pais = pais
        self.ciudad = ciudad
        self.imagen = imagen
        self.entrenadores = entrenadores if entrenadores is not None else []
        self.nadadores = nadadores if nadadores is not None else []
