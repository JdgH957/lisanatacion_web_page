from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relación con entrenadores y deportistas (opcional)
    rol = Column(String, nullable=False)  # 'admin', 'entrenador', 'deportista', 'normal'
