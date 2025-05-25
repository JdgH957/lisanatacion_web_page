from abc import ABC, abstractmethod
from app.application.DTOS.entrenador_dto import EntrenadorCreateDTO, EntrenadorOutDTO, EntrenadorUpdateDTO


class IEntrenadorService(ABC):
    @abstractmethod
    def crear_entrenador(self, entrenador_dto: EntrenadorCreateDTO) -> EntrenadorOutDTO:
        pass

    @abstractmethod
    def get_entrenador_by_id(self, entrenador_id: int) -> EntrenadorOutDTO:
        pass

    @abstractmethod
    def get_entrenadores(self) -> list[EntrenadorOutDTO]:
        pass

    @abstractmethod
    def eliminar_entrenador(self, entrenador_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_entrenador(self, entrenador_id: int, entrenador_dto: EntrenadorUpdateDTO) -> EntrenadorOutDTO:
        pass

    @abstractmethod
    def agregar_nadador(self, entrenador_id: int, nadador_id: int) -> EntrenadorOutDTO:
        pass