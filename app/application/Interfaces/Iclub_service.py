from abc import ABC, abstractmethod
from app.application.DTOS.club_dto import ClubCreateDTO, ClubOutDTO, ClubUpdateDTO

class IClubService(ABC):
    @abstractmethod
    def crear_club(self, club_dto: ClubCreateDTO) -> ClubOutDTO:
        pass

    @abstractmethod
    def get_club_by_id(self, club_id: int) -> ClubOutDTO:
        pass

    @abstractmethod
    def get_clubes(self) -> list[ClubOutDTO]:
        pass

    @abstractmethod
    def eliminar_club(self, club_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_club(self, club_id: int, club_dto: ClubUpdateDTO) -> ClubOutDTO:
        pass