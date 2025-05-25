# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.infrastructure.db.DBModels.usuario_orm import UsuarioORM
from app.core.auth.auth import verify_password
from app.core.auth.jwt import crear_token


router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(UsuarioORM).filter(UsuarioORM.email == form_data.username).first()
    if not usuario or not verify_password(form_data.password, usuario.contra):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = crear_token({"sub": usuario.email, "rol": usuario.rol})
    return {"access_token": token, "token_type": "bearer","usuario": {
            "nombre": usuario.nombre,
            "apellido":usuario.apellido,
            "fecha_asig":usuario.fecha_asig,
            "email": usuario.email,
            "rol": usuario.rol,
            "contacto":usuario.contacto,
            "edad":usuario.edad
        }}
