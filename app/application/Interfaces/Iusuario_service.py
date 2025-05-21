from abc import ABC, abstractmethod
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO

class IUsuarioService(ABC):
    @abstractmethod
    def crear_usuario(self, usuario_dto: UsuarioCreateDTO) -> UsuarioOutDTO:
        pass
