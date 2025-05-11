from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.entrenadores import Entrenador

def eliminar_entrenador(entrenador_id: int, db: Session):
    entrenador = db.query(Entrenador).filter(Entrenador.id == entrenador_id).first()
    if not entrenador:
        raise HTTPException(status_code=404, detail="entrenador no encontrado")

    db.delete(entrenador)
    db.commit()
    return {"msg": f"Entrenador con ID {entrenador_id} eliminado correctamente"}
