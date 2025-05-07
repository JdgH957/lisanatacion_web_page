from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuarios import Usuario
from app.auth import hash_password
from typing import List, Optional

def listar_usuarios(db: Session) -> List[Usuario]:
    return db.query(Usuario).all()

def obtener_usuario_por_id(usuario_id: int, db: Session) -> Optional[Usuario]:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
