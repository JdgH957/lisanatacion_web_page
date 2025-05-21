from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.crud import crud_usuarios
from app.config.dependencies.admin import get_current_admin  


from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO
from app.config.dependencies import get_usuario_service


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/usuarios", response_model=UsuarioOutDTO)
def crear_usuario(usuario: UsuarioCreateDTO, usuario_service=Depends(get_usuario_service)):
    return usuario_service.crear_usuario(usuario)

@router.get("/", summary="Listar todos los usuarios (solo admin)")
def listar_usuarios(
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_usuarios.listar_usuarios(db)

@router.get("/{usuario_id}", summary="Obtener usuario por ID (solo admin)")
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    usuario = crud_usuarios.obtener_usuario_por_id(usuario_id, db)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", summary="Actualizar usuario (solo admin)")
def actualizar_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_usuarios.actualizar_usuario(usuario_id, usuario, db)


@router.delete("/{usuario_id}", summary="Eliminar usuario (solo admin)")
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_usuarios.eliminar_usuario(usuario_id, db)