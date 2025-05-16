# app/routes/protegida.py
from fastapi import APIRouter, Depends, HTTPException
from app.core.auth.jwt_bearer import JwtBearer

router = APIRouter()

@router.get("/solo-admin")
def ruta_admin(payload: dict = Depends(JwtBearer())):
    if payload.get("rol") != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return {"mensaje": "¡Hola Admin!"}
