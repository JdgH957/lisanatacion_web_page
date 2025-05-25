from http.client import HTTPException
from typing import List
from app.Domain.models.usuario import Usuario
from app.application.Interfaces.Iusuario_service import IUsuarioService
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO, UsuarioUpdateDTO
from app.Domain.Irepos.Iusuario_repo import IUsuarioRepository
from app.core.auth.auth import hash_password
from app.Domain.mappers.usuario_mapper import dominio_a_dto_out, dominio_a_orm, dto_create_a_dominio, dto_update_a_dominio


class UsuarioService(IUsuarioService):

    def __init__(self, usuario_repo: IUsuarioRepository):
        self.usuario_repo = usuario_repo

    def crear_usuario(self, usuario_dto: UsuarioCreateDTO) -> UsuarioOutDTO:
        usuario = dto_create_a_dominio(usuario_dto)
        if self.usuario_repo.existe_email(usuario.email):
            raise ValueError("El email ya está registrado")

        usuario.contra = hash_password(usuario.contra)
        usuario_creado, usuario_id = self.usuario_repo.crear_usuario(usuario)

        return dominio_a_dto_out(usuario_creado, usuario_id)
    
    def get_usuarios(self) -> List[UsuarioOutDTO]:
        usuarios = self.usuario_repo.get_usuarios()
        return [dominio_a_dto_out(u) for u in usuarios]
    
    def get_usuario_by_id(self, usuario_id: int) -> UsuarioOutDTO:
        usuario = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return dominio_a_dto_out(usuario)
    
    def eliminar_usuario(self, usuario_id: int) -> None:
        usuario = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado, no puede eliminarse")
        self.usuario_repo.eliminar_usuario(usuario_id)

    def actualizar_usuario(self, usuario_id: int, usuario_dto: UsuarioUpdateDTO) -> UsuarioOutDTO:
        usuario_existente = self.usuario_repo.get_usuario_by_id(usuario_id)
        if not usuario_existente:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Creamos un nuevo usuario a partir del existente
        usuario_actualizado = Usuario(
            nombre=usuario_dto.nombre or usuario_existente.nombre,
            apellido=usuario_dto.apellido or usuario_existente.apellido,
            email=usuario_dto.email or usuario_existente.email,
            contra=hash_password(usuario_dto.contra) if usuario_dto.contra else usuario_existente.contra,
            rol=usuario_existente.rol,  # suponiendo que el rol no cambia
        )

        usuario_final = self.usuario_repo.actualizar_usuario(usuario_id, usuario_actualizado)
        return dominio_a_dto_out(usuario_final)
