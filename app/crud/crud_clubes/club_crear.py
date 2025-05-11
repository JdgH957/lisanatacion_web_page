from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.clubes import Club
from app.api.schemas import ClubCreate


def crear_club(club: ClubCreate, db: Session):
    existente = db.query(Club).filter(Club.nombre_club == club.nombre_club).first()

    if existente:
        raise HTTPException(status_code=400, detail="El nombre del club ya está registrado")

    club_db = Club(
        nombre_club=club.ombre_club,
        fecha_creacion=club.fecha_creacion,
        lider_id =club.titulos,
        email =club.email,
    )
    
    db.add(club_db)
    db.commit()
    db.refresh(club_db)

    return club_db