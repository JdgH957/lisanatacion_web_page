from sqlalchemy import Column, Integer, String, Date, Enum
from app.database import Base
import enum

class RolUsuarioEnum(str, enum.Enum):
    admin = "admin"
    entrenador = "entrenador"
    club = "club"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contra = Column(String, nullable=False)
    fecha_asig = Column(Date, nullable=False)
    rol = Column(Enum(RolUsuarioEnum), nullable=False)
    contacto = Column(Integer, unique=True, nullable=True)
    edad = Column(Integer, nullable=True)



    


    
