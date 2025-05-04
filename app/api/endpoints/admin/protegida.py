# app/routes/protegida.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
router = APIRouter()

@router.get("/solo-admin")
def ruta_admin(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload or payload.get("rol") != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return {"mensaje": "¡Hola Admin!"}
