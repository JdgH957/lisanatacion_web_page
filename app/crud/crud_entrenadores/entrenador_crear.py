from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.entrenadores import Entrenador
from app.auth import hash_password
from app.api.schemas import EntrenadorCreate


def crear_entrenador(entrenador: EntrenadorCreate, db: Session):
    existente = db.query(Entrenador).filter(Entrenador.email == entrenador.email).first()

    if existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    entrenador_db = Entrenador(
        nombre=entrenador.nombre,
        apellido=entrenador.apellido,
        email=entrenador.email,
        fecha_asig=entrenador.fecha_asig,
        titulos=entrenador.titulos,
        experiencia=entrenador.experiencia,
        años_exp=entrenador.años_exp,
        club_id=entrenador.club_id,
    )
    
    db.add(entrenador_db)
    db.commit()
    db.refresh(entrenador_db)

    return entrenador_db