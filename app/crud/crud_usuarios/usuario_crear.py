from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuarios import Usuario
from app.models.entrenadores import Entrenador
from app.models.clubes import Club
from app.api.schemas import UsuarioCreate
from app.auth import hash_password

def crear_usuario(usuario: UsuarioCreate, db: Session):
    existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    usuario_db = Usuario(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        contra=hash_password(usuario.contra),
        fecha_asig=usuario.fecha_asig,
        rol=usuario.rol.value,
        contacto=usuario.contacto,
        edad=usuario.edad
    )
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)

    if usuario.rol.value == "entrenador":
        entrenador_db = Entrenador(
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            email=usuario.email,
            fecha_asig=usuario.fecha_asig
        )
        db.add(entrenador_db)
        db.commit()

    elif usuario.rol.value == "club":
        if not usuario.fecha_asig:
            raise HTTPException(status_code=400, detail="Se requiere fecha de creación para un club")

        club_db = Club(
            nombre_club=usuario.nombre,  
            fecha_creacion=usuario.fecha_asig,
            email=usuario.email
        )
        db.add(club_db)
        db.commit()

    return usuario_db
