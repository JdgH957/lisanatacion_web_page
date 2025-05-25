from fastapi import Depends
from sqlalchemy.orm import Session
from app.Domain.use_cases.entrenador_service import EntrenadorService
from app.infrastructure.db.repositories.usuario_repo import UsuarioRepository
from app.Domain.use_cases.usuario_service import UsuarioService
from app.infrastructure.db.repositories.entrenador_repo import EntrenadorRepository
from app.Domain.use_cases.nadador_service import NadadorService
from app.infrastructure.db.repositories.nadador_repo import NadadorRepository
from app.Domain.use_cases.club_service import ClubService
from app.infrastructure.db.repositories.club_repo import ClubRepository
from app.database import get_db  # función que retorna la sesión de DB

def get_usuario_service(db: Session = Depends(get_db)):
    usuario_repo = UsuarioRepository(db)
    return UsuarioService(usuario_repo)

def get_entrenador_service(db: Session = Depends(get_db)):
    entrenador_repo = EntrenadorRepository(db)
    return EntrenadorService(entrenador_repo)

def get_nadador_service(db: Session = Depends(get_db)):
    nadador_repo = NadadorRepository(db)
    return NadadorService(nadador_repo)

def get_club_service(db: Session = Depends(get_db)):
    club_repo = ClubRepository(db)
    return ClubService(club_repo)

