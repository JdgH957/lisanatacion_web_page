from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Tabla intermedia para la relación muchos a muchos entre Club y Usuario
club_entrenadores = Table(
    "club_entrenadores",
    Base.metadata,
    Column("club_id", Integer, ForeignKey("clubes.id"), primary_key=True),
    Column("entrenador_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    contra = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    fecha_asig = Column(Date, nullable=False)
    rol = Column(String, nullable=False)  # 'admin', 'entrenador', 'deportista', 'normal'

    # Relación con Clubes (solo si el usuario es entrenador)
    clubs = relationship("Club", secondary=club_entrenadores, back_populates="entrenadores")

class Club(Base):
    __tablename__ = "clubes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    
    # Relación con Entrenadores
    entrenadores = relationship("Usuario", secondary=club_entrenadores, back_populates="clubs")

