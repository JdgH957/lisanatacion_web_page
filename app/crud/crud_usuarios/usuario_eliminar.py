from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuarios import Usuario
from app.auth import hash_password


def eliminar_usuario(usuario_id: int, db: Session):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()
    return {"msg": f"Usuario con ID {usuario_id} eliminado correctamente"}
