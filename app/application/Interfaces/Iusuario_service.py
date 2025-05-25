from abc import ABC, abstractmethod
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO,UsuarioUpdateDTO

class IUsuarioService(ABC):

    @abstractmethod
    def crear_usuario(self, usuario_dto: UsuarioCreateDTO) -> UsuarioOutDTO:
        pass

    @abstractmethod
    def get_usuario_by_id(self, usuario_id: int) -> UsuarioOutDTO:
        pass

    @abstractmethod
    def get_usuarios(self) -> list[UsuarioOutDTO]:
        pass

    @abstractmethod
    def eliminar_usuario(self, usuario_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_usuario(self, usuario_id: int, usuario_dto: UsuarioUpdateDTO) -> UsuarioOutDTO:
        pass
