
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MiembroORM(Base):
    __tablename__ = "miembros"

    id_miembro = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id_curso"), nullable=False)
    tipo_miembro = Column(String, nullable=False)  # Ej: "titular", "suplente", etc.
    estado_pago = Column(String, nullable=False)   # Ej: "pendiente", "pagado"

    curso = relationship("CursoORM", backref="miembros")
