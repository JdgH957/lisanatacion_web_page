
from typing import List
from app.application.Interfaces.Inadador_service import INadadorService
from app.Domain.Irepos.Inadador_repo import INadadorRepository
from app.application.DTOS.nadador_dto import NadadorCreateDTO, NadadorUpdateDTO, NadadorOutDTO

class NadadorService(INadadorService):
    def __init__(self, nadador_repository: INadadorRepository):
        self.nadador_repository = nadador_repository

    def get_nadadores(self) -> List[NadadorOutDTO]:
        return self.nadador_repository.get_nadadores()

    def get_nadador_by_id(self, nadador_id: int) -> NadadorOutDTO:
        return self.nadador_repository.get_nadador_by_id(nadador_id)

    def crear_nadador(self, nadador_dto: NadadorCreateDTO) -> NadadorOutDTO:
        return self.nadador_repository.crear_nadador(nadador_dto)

    def actualizar_nadador(self, nadador_id: int, nadador_dto: NadadorUpdateDTO) -> NadadorOutDTO:
        return self.nadador_repository.actualizar_nadador(nadador_id, nadador_dto)

    def eliminar_nadador(self, nadador_id: int) -> None:
        self.nadador_repository.eliminar_nadador(nadador_id)