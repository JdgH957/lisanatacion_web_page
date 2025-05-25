from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base  

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_fundacion = Column(String, nullable=False)  # Si es Date, cámbialo a Column(Date)
    pais = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    imagen = Column(String, nullable=True)

    entrenadores = relationship("Entrenador", back_populates="club")
    nadadores = relationship("Nadador", back_populates="club")
