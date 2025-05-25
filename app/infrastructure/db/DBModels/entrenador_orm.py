from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class EntrenadorORM(Base):
    __tablename__ = "entrenadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    rol = Column(String, nullable=False) 
    contacto = Column(String)
    edad = Column(Integer)
    disciplinas = Column(JSON, nullable=False)  
    categorias = Column(JSON, nullable=False)   
    experiencia = Column(String)
    imagen = Column(String)
    id_club = Column(Integer, ForeignKey("clubes.id"))

    club = relationship("ClubORM", back_populates="entrenadores")
    nadadores = relationship("NadadorORM", back_populates="entrenador")
