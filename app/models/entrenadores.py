from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Entrenador(Base):
    __tablename__ = "entrenadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)  # no es único, porque puede haber historial
    fecha_asig = Column(Date, nullable=False)
    club_actual = Column(String, nullable=True)
    titulos = Column(String, nullable=True)  # podrías usar una tabla aparte para más detalle
    experiencia = Column(String, nullable=True)
    