# app/auth/jwt.py
import time
from typing import Dict, Literal, Union
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM, EXPIRATION_ACCESS_MINUTES, EXPIRATION_REFRESH_MINUTES

def _sign_token(payload: dict, minutes_expire: int, token_type: Literal["ACCESS", "REFRESH"]) -> str:
    expire_ts = int(time.time() + minutes_expire * 60)
    payload.update({"expires": expire_ts, "type": token_type})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def sign_access_token(user_id: str, role: str) -> str:
    return _sign_token({"sub": user_id, "rol": role}, EXPIRATION_ACCESS_MINUTES, "ACCESS")

def sign_refresh_token(user_id: str) -> str:
    return _sign_token({"sub": user_id}, EXPIRATION_REFRESH_MINUTES, "REFRESH")

def decode_token(token: str, expected_type: Literal["ACCESS", "REFRESH"]) -> Union[Dict, None]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != expected_type:
            return None
        if time.time() > float(payload.get("expires", 0)):
            return None
        return payload
    except JWTError:
        return None
