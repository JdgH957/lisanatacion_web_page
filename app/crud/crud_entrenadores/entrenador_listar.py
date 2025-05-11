from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.entrenadores import Entrenador
from typing import List, Optional

def listar_entrenadores(db: Session) -> List[Entrenador]:
    return db.query(Entrenador).all()

def obtener_entrenador_por_id(entrenador_id: int, db: Session) -> Optional[Entrenador]:
    entrenador = db.query(Entrenador).filter(Entrenador.id == entrenador_id).first()
    if not entrenador:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return entrenador