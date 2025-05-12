from sqlalchemy import Column, ForeignKey, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

class Deportista(Base):
    __tablename__ = "deportistas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    peso = Column(Integer, nullable=False)
    disciplina = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    foto = Column(String, nullable=True)
