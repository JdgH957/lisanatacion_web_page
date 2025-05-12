# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.auth_schemas import LoginRequest
from app.database import get_db
from app.models import Usuario
from app.auth.auth import verify_password
from app.core.auth.jwt import sign_access_token, sign_refresh_token

router = APIRouter()

@router.post("/login")
def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.email).first()

    if not usuario or not verify_password(form_data.password, usuario.contra):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = sign_access_token(usuario.email, usuario.rol)
    refresh_token = sign_refresh_token(usuario.email)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
