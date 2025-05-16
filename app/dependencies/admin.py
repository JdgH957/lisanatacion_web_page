from fastapi import Depends, HTTPException
from app.core.auth.jwt_bearer import JwtBearer

def get_current_admin(payload: dict = Depends(JwtBearer())):
    if payload.get("rol") != "admin":
        raise HTTPException(status_code=403, detail="Acceso solo para administradores")
    return payload
