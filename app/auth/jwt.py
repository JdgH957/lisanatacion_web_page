# app/auth/jwt.py
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "tu_clave_secreta_super_segura"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def crear_token(data: dict):
    # Asegurarse de que el token contiene la fecha de expiración
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    datos.update({"exp": expiracion})
    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        # Decodificar el token usando la clave secreta y el algoritmo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Verificar si la clave 'exp' está presente y si el token ha expirado
        if datetime.utcnow() > datetime.utcfromtimestamp(payload["exp"]):
            raise JWTError("Token ha expirado")

        # Si todo está bien, devolver el payload
        return payload

    except JWTError:
        return None
