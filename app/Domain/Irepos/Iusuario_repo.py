from abc import ABC, abstractmethod
from typing import List, Optional
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioUpdateDTO
from app.Domain.models.usuario import Usuario


class IUsuarioRepository(ABC):

    @abstractmethod
    def existe_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def crear_usuario(self, usuario: Usuario) -> tuple[Usuario,int]:
        pass

    @abstractmethod
    def get_usuarios(self) -> List[Usuario]:
        pass

    @abstractmethod
    def get_usuario_by_id(self, usuario_id: int) -> Usuario:
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_usuario(self, usuario_id: int, usuario: Usuario) -> Usuario:
        pass
