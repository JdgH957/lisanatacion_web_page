from app.application.Interfaces.Iusuario_service import IUsuarioService
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO
from app.infrastructure.db.repositories.usuario_repo import IUsuarioRepository
from app.auth import hash_password

class UsuarioService(IUsuarioService):
    def __init__(self, usuario_repo: IUsuarioRepository):
        self.usuario_repo = usuario_repo

    def crear_usuario(self, usuario_dto: UsuarioCreateDTO) -> UsuarioOutDTO:
        if self.usuario_repo.existe_email(usuario_dto.email):
            raise ValueError("El email ya está registrado")

        usuario_dto.contra = hash_password(usuario_dto.contra)
        usuario_creado = self.usuario_repo.crear_usuario(usuario_dto)

        return UsuarioOutDTO.from_orm(usuario_creado)
