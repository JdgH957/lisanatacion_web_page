from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CursoORM(Base):
    __tablename__ = "cursos"

    id_curso = Column(Integer, primary_key=True, index=True)
    piscina_id = Column(Integer, ForeignKey("piscinas.id_piscina"), nullable=False)
    entrenador_id = Column(Integer, ForeignKey("entrenadores.id"), nullable=False)
    categoria = Column(String, nullable=False)
    max_cupos = Column(Integer, nullable=False)
    cantidad_miembros = Column(Integer, nullable=False, default=0)
    disciplina = Column(String, nullable=False)
    precio_mes = Column(Float, nullable=False)
    precio_prueba = Column(Float, nullable=False)
    descripcion = Column(String, nullable=True)

    piscina = relationship("PiscinaORM")
    entrenador = relationship("EntrenadorORM")
