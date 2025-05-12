import time
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.status import HTTP_403_FORBIDDEN
from app.core.auth.jwt import decode_token

class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid authentication scheme.")
        payload = decode_token(credentials.credentials, expected_type="ACCESS")
        if not payload:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid or expired token.")
        return payload
