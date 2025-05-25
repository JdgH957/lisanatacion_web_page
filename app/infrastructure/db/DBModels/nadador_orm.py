from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class NadadorORM(Base):
    __tablename__ = "nadadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer)
    peso = Column(Integer) 
    categoria = Column(String) 
    disciplina = Column(String)  
    nivel = Column(String)
    experiencia = Column(String)
    imagen = Column(String)

    id_entrenador = Column(Integer, ForeignKey("entrenadores.id"))
    id_club = Column(Integer, ForeignKey("clubes.id"))

    entrenador = relationship("EntrenadorORM", back_populates="nadadores")
    club = relationship("ClubORM", back_populates="nadadores")
