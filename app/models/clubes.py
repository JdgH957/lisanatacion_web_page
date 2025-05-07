from sqlalchemy import Column, ForeignKey, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Club(Base):
    __tablename__ = "clubes"

    id = Column(Integer, primary_key=True, index=True)
    nombre_club = Column(String, nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    lider_id = Column(Integer, ForeignKey("entrenadores.id"), nullable=False)
    email = Column(String, nullable=False)

    lider = relationship("Entrenador", foreign_keys=(lider_id))
    entrenadores = relationship("Entrenador", back_populates="club")
