from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


contraseña = "123456"
hashed = hash_password(contraseña)
print(f"Contraseña: {contraseña}")
print(f"Contraseña hasheada: {hashed}")