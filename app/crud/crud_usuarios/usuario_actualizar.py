from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuarios import Usuario
from app.api.schemas import UsuarioUpdate
from app.auth import hash_password
from typing import List, Optional

def actualizar_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: Session):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.nombre = usuario_update.nombre or usuario.nombre
    usuario.apellido = usuario_update.apellido or usuario.apellido
    usuario.email = usuario_update.email or usuario.email
    usuario.rol = usuario_update.rol.value or usuario.rol
    if usuario_update.contra:
        usuario.contra = hash_password(usuario_update.contra)
    if usuario_update.fecha_asig:
        usuario.fecha_asig = usuario_update.fecha_asig

    db.commit()
    db.refresh(usuario)
    return usuario