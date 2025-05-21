from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.infrastructure.db.DBModels.entrenador_orm import Entrenador
from app.api.schemas import EntrenadorUpdate
from typing import List, Optional

def actualizar_entrenador(entrenador_id: int, entrenador_update: EntrenadorUpdate, db: Session):
    entrenador = db.query(Entrenador).filter(Entrenador.id == entrenador_id).first()
    if not entrenador:
        raise HTTPException(status_code=404, detail="Entrenador no encontrado")

    entrenador.nombre = entrenador_update.nombre or entrenador.nombre
    entrenador.apellido = entrenador_update.apellido or entrenador.apellido
    entrenador.email = entrenador_update.email or entrenador.email
    entrenador.fecha_asig = entrenador_update.fecha_asig or entrenador.fecha_asig
    entrenador.titulos = entrenador_update.titulos or entrenador.titulos
    entrenador.experiencia = entrenador_update.experiencia or entrenador.experiencia
    entrenador.años_exp = entrenador_update.años_exp or entrenador.años_exp
    entrenador.club_id = entrenador_update.club_id or entrenador.club_id
        
    db.commit()
    db.refresh(entrenador)
    return entrenador