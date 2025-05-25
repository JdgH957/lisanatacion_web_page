from http.client import HTTPException
from typing import List
from app.application.Interfaces.Iusuario_service import IUsuarioService
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO, UsuarioUpdateDTO
from app.Domain.Irepos.Iusuario_repo import IUsuarioRepository
from app.core.auth.auth import hash_password
from app.Domain.mappers.usuario_mapper import actualizar_usuario_con_dto,dto_create_a_dominio


class UsuarioService(IUsuarioService):

    def __init__(self, usuario_repo: IUsuarioRepository):
        self.usuario_repo = usuario_repo

    def crear_usuario(self, usuario_dto: UsuarioCreateDTO) -> UsuarioOutDTO:
        usuario = dto_create_a_dominio(usuario_dto)
        if self.usuario_repo.existe_email(usuario.email):
            raise ValueError("El email ya está registrado")

        usuario.contra = hash_password(usuario.contra)
        usuario_creado= self.usuario_repo.crear_usuario(usuario)

        return UsuarioOutDTO.model_validate(usuario_creado.__dict__)
    
    def get_usuarios(self) -> List[UsuarioOutDTO]:
        usuarios = self.usuario_repo.get_usuarios()
        return [UsuarioOutDTO.model_validate(u.__dict__) for u in usuarios]
    
    def get_usuario_by_id(self, usuario_id: int) -> UsuarioOutDTO:
        usuario = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return UsuarioOutDTO.model_validate(usuario.__dict__)
    
    def eliminar_usuario(self, usuario_id: int) -> None:
        usuario = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado, no puede eliminarse")
        self.usuario_repo.eliminar_usuario(usuario_id)

    def actualizar_usuario(self, usuario_id: int, usuario_dto: UsuarioUpdateDTO) -> UsuarioOutDTO:
        usuario_existente = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario_existente:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        usuario_actualizado = actualizar_usuario_con_dto(usuario_existente, usuario_dto)
        usuario_actualizado = self.usuario_repo.actualizar_usuario(usuario_id, usuario_actualizado)
        return UsuarioOutDTO.model_validate(usuario_actualizado.__dict__)
