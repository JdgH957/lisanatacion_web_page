from fastapi import APIRouter, Depends
from app.Domain.use_cases.usuario_service import UsuarioService
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO, UsuarioUpdateDTO
from app.config.dependencies.dependencies import get_usuario_service


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/crear", response_model=UsuarioOutDTO)
def crear_usuario(usuario: UsuarioCreateDTO, usuario_service: UsuarioService = Depends(get_usuario_service)):
    return usuario_service.crear_usuario(usuario)


@router.get("/lista",response_model=list[UsuarioOutDTO], summary="Listar todos los usuarios")
def get_usuarios(usuario_service: UsuarioService = Depends(get_usuario_service)):
    return usuario_service.get_usuarios()


@router.get("/{usuario_id}", response_model=UsuarioOutDTO, summary="Obtener usuario por ID")
def get_usuario(usuario_id: int, usuario_service: UsuarioService = Depends(get_usuario_service)):
    return usuario_service.get_usuario_by_id(usuario_id)

@router.delete("/eliminar/{usuario_id}", summary = "Elimina el usuario por ID")
def eliminar_usuario(usuario_id: int, usuario_service: UsuarioService = Depends(get_usuario_service)):
    return usuario_service.eliminar_usuario(usuario_id)

@router.put("/actualizar/{usuario_id}", response_model=UsuarioOutDTO, summary="Actualizar usuario por ID")
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdateDTO, usuario_service: UsuarioService = Depends(get_usuario_service)):
    return usuario_service.actualizar_usuario(usuario_id, usuario)
