from abc import ABC, abstractmethod
from typing import List
from app.Domain.models.entrenador import Entrenador

class IEntrenadorRepository(ABC):

    @abstractmethod
    def crear_entrenador(self, entrenador: Entrenador) -> Entrenador:
        pass

    @abstractmethod
    def get_entrenadores(self) -> List[Entrenador]:
        pass

    @abstractmethod
    def get_entrenador_by_id(self, entrenador_id: int) -> Entrenador:
        pass

    @abstractmethod
    def eliminar_entrenador(self, entrenador_id: int) -> None:
        pass

    @abstractmethod
    def actualizar_entrenador(self, entrenador_id: int, entrenador: Entrenador) -> Entrenador:
        pass

    @abstractmethod
    def agregar_nadador(self, entrenador_id: int, nadador_id: int) -> Entrenador:
        pass