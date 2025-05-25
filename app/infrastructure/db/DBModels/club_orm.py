from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.orm import relationship
from app.database import Base  

class ClubORM(Base):
    __tablename__ = "clubes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_fundacion = Column(String, nullable=False)  # Si es Date, cámbialo a Column(Date)
    pais = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    imagen = Column(String, nullable=True)

    entrenadores = relationship("EntrenadorORM", back_populates="club")
    nadadores = relationship("NadadorORM", back_populates="club")
