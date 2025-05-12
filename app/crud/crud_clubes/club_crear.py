from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.clubes import Club
from app.api.schemas import ClubCreate
from app.models.entrenadores import Entrenador


def crear_club(club: ClubCreate, db: Session):
    existente = db.query(Club).filter(Club.nombre_club == club.nombre_club).first()

    if existente:
        raise HTTPException(status_code=400, detail="El nombre del club ya está registrado")

    club_db = Club(
        nombre_club=club.nombre_club,
        fecha_creacion=club.fecha_creacion,
        email =club.email,
        lider_id=club.lider_id,
    )

    db.add(club_db)
    db.commit()
    db.refresh(club_db)

    for entrenador_id in club.entrenadores_ids:
        entrenador = db.query(Entrenador).filter(Entrenador.id == entrenador_id).first()
        if not entrenador:
            raise HTTPException(status_code=404, detail=f"Entrenador {entrenador_id} no encontrado")
        if entrenador.club_id is not None:
            raise HTTPException(status_code=400, detail=f"El entrenador {entrenador_id} ya está en un club")

        entrenador.club_id = club_db.id
        db.add(entrenador)

    db.commit()
    return club_db