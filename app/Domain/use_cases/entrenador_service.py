
from http.client import HTTPException
from app.application.Interfaces.Ientrenador_service import IEntrenadorService
from app.application.DTOS.entrenador_dto import EntrenadorCreateDTO, EntrenadorOutDTO, EntrenadorUpdateDTO
from app.Domain.Irepos.Ientrenador_repo import IEntrenadorRepository
from app.Domain.mappers.entrenador_mapper import actualizar_entrenador_con_dto, dominio_a_dto_out, dto_a_dominio, dto_update_a_dominio

class EntrenadorService(IEntrenadorService):

    def __init__(self, entrenador_repo: IEntrenadorRepository):
        self.entrenador_repo = entrenador_repo

    def crear_entrenador(self, entrenador_dto: EntrenadorCreateDTO) -> EntrenadorOutDTO:
        entrenador = dto_a_dominio(entrenador_dto)
        entrenador = self.entrenador_repo.crear_entrenador(entrenador)
        if not entrenador:
            raise ValueError("Error al crear el entrenador")
        return dominio_a_dto_out(entrenador)
    
    def get_entrenadores(self) -> list[EntrenadorOutDTO]: 
        entrenadores = self.entrenador_repo.get_entrenadores()
        return [dominio_a_dto_out(e) for e in entrenadores]
    
    def get_entrenador_by_id(self, entrenador_id: int) -> EntrenadorOutDTO:
        entrenador = self.entrenador_repo.get_entrenador_by_id(entrenador_id)
        if not entrenador:
            raise ValueError("Entrenador no encontrado")
        return dominio_a_dto_out(entrenador)
    
    def eliminar_entrenador(self, entrenador_id: int) -> None:
        self.entrenador_repo.eliminar_entrenador(entrenador_id)
        return None

    def actualizar_entrenador(self, entrenador_id: int, entrenador_dto: EntrenadorUpdateDTO) -> EntrenadorOutDTO:
        entrenador = self.entrenador_repo.get_entrenador_by_id(entrenador_id)
        if not entrenador:
            raise ValueError("Entrenador no encontrado")
    
        entrenador_actualizado = actualizar_entrenador_con_dto(entrenador, entrenador_dto)
        entrenador_actualizado = self.entrenador_repo.actualizar_entrenador(entrenador_id, entrenador_actualizado)
        return dominio_a_dto_out(entrenador_actualizado)


    def agregar_nadador(self, entrenador_id: int, nadador_id: int) -> EntrenadorOutDTO:
        entrenador = self.entrenador_repo.get_entrenador_by_id(entrenador_id)
        if not entrenador:
            raise HTTPException(status_code=404, detail="Entrenador no encontrado")
        entrenador_nuevo = self.entrenador_repo.agregar_nadador(entrenador_id, nadador_id)
        return dominio_a_dto_out(entrenador_nuevo)