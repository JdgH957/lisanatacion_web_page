from pydantic import BaseModel
from typing import Optional

class CursoCreateDTO(BaseModel):
    piscina_id: int
    entrenador_id: int
    categoria: str
    max_cupos: int
    disciplina: str
    precio_mes: float
    precio_prueba: float
    descripcion: Optional[str] = None

class CursoOutDTO(CursoCreateDTO):
    id_curso: int
    cantidad_miembros: int

    class Config:
        orm_mode = True
