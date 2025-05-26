from pydantic import BaseModel
from typing import List, Optional

from app.application.common.enums import DiaSemanaEnum, MesEnum


class HorarioCreateDTO(BaseModel):
    piscina_id: int
    curso_id: Optional[int] = None
    dia: DiaSemanaEnum
    mes: MesEnum
    hora_inicio: str
    precio: float
    disponible: bool = True


class HorarioOutDTO(HorarioCreateDTO):
    id_horario: int

    class Config:
        orm_mode = True

class HorarioFiltroDTO(BaseModel):
    piscina_id: int
    dia: DiaSemanaEnum
    mes: MesEnum

class ReservaHorariosCursoNuevoRequest(BaseModel):
    horario_ids: List[int]
    id_entrenador: int
    categoria: str
    max_cupos: int
    disciplina: str
    precio_mes: float
    precio_prueba: float
    descripcion: str