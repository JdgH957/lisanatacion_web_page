from abc import ABC, abstractmethod
from app.application.DTOS.nadador_dto import NadadorCreateDTO, NadadorOutDTO, NadadorUpdateDTO


class INadadorService(ABC):
    @abstractmethod
    def crear_nadador(self, nadador_dto: NadadorCreateDTO) -> NadadorOutDTO:
        pass

    @abstractmethod
    def get_nadador_by_id(self, nadador_id: int) -> NadadorOutDTO:
        pass

    @abstractmethod
    def get_nadadores(self) -> list[NadadorOutDTO]:
        pass

    @abstractmethod
    def eliminar_nadador(self, nadador_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_nadador(self, nadador_id: int, nadador_dto: NadadorUpdateDTO) -> NadadorOutDTO:
        pass