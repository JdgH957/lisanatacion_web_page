from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class PiscinaORM(Base):
    __tablename__ = "piscinas"

    id_piscina = Column(Integer, primary_key=True, index=True)
    aforo_maximo = Column(Integer, nullable=False)
    profundidad = Column(Float, nullable=False)
    tipo_piscina = Column(String, nullable=False)
    largo = Column(Float, nullable=False)
    ancho = Column(Float, nullable=False)
