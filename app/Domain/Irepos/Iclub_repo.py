from abc import ABC, abstractmethod
from app.Domain.models.club import Club


class IclubRepository(ABC):

    @abstractmethod
    def crear_club(self, club: Club) -> Club:
        pass

    @abstractmethod
    def get_clubes(self) -> list[Club]:
        pass

    @abstractmethod
    def get_club_by_id(self, club_id: int) -> Club:
        pass

    @abstractmethod
    def actualizar_club(self, club: Club) -> Club:
        pass

    @abstractmethod
    def eliminar_club(self, club_id: int) -> None:
        pass