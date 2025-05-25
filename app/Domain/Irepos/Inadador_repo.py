from abc import ABC, abstractmethod
from app.Domain.models.nadador import Nadador

class INadadorRepo(ABC):

    @abstractmethod
    def crear_nadador(self, nadador: Nadador) -> Nadador:
        pass

    @abstractmethod
    def get_nadador_by_id(self, nadador_id: int) -> Nadador:
        pass

    @abstractmethod
    def get_nadadores(self) -> list[Nadador]:
        pass

    @abstractmethod
    def eliminar_nadador(self, nadador_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_nadador(self, nadador: Nadador) -> Nadador:
        pass