from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import verificar_token
from app.auth.jwt import SECRET_KEY, ALGORITHM 
from app.database import get_db
from app.models.usuarios import Usuario
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.auth.jwt import verificar_token 
from sqlalchemy.orm import Session

# Definir el objeto OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verificar_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido o ha expirado")

    email = payload.get("sub")
    rol = payload.get("rol")

    # Verificar si el rol es 'admin'
    if rol != "admin":
        raise HTTPException(status_code=401, detail="No autorizado")

    # Verificar si el usuario existe en la base de datos
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    return {"email": email, "rol": rol}