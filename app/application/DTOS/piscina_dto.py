from pydantic import BaseModel, Field
from typing import Optional

class PiscinaCreateDTO(BaseModel):
    aforo_maximo: int = Field(..., gt=0)
    profundidad: float = Field(..., gt=0)
    tipo_piscina: str
    largo: float = Field(..., gt=0)
    ancho: float = Field(..., gt=0)


class PiscinaOutDTO(BaseModel):
    id_piscina: int
    aforo_maximo: int
    profundidad: float
    tipo_piscina: str
    largo: float
    ancho: float

    class Config:
        orm_mode = True

class PiscinaUpdateDTO(BaseModel):
    aforo_maximo: Optional[int] = Field(None, gt=0)
    profundidad: Optional[float] = Field(None, gt=0)
    tipo_piscina: Optional[str]
    largo: Optional[float] = Field(None, gt=0)
    ancho: Optional[float] = Field(None, gt=0)
