from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.infrastructure.db.DBModels.curso_orm import CursoORM


class HorarioORM(Base):
    __tablename__ = "horarios"

    id_horario = Column(Integer, primary_key=True, index=True)
    piscina_id = Column(Integer, ForeignKey("piscinas.id_piscina"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id_curso"), nullable=True)
    dia = Column(String, nullable=False)
    mes = Column(String, nullable=False)
    hora_inicio = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, nullable=False, default=True)

    piscina = relationship("PiscinaORM")
    curso = relationship(CursoORM)
