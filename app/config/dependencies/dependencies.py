from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.repositories.usuario_repo import UsuarioRepository
from app.Domain.use_cases.usuario_services import UsuarioService
from app.database import get_db  # función que retorna la sesión de DB

def get_usuario_service(db: Session = Depends(get_db)):
    usuario_repo = UsuarioRepository(db)
    return UsuarioService(usuario_repo)
