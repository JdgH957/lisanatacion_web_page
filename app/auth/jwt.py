# app/auth/jwt.py
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "tu_clave_secreta_super_segura"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def crear_token(data: dict):
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    datos.update({"exp": expiracion})
    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
