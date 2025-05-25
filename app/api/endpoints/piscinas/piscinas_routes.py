from fastapi import APIRouter, Depends
from app.application.DTOS.piscina_dto import PiscinaCreateDTO, PiscinaOutDTO, PiscinaUpdateDTO
from app.Domain.use_cases.piscina_service import PiscinaService
from app.config.dependencies.dependencies import get_piscina_service



router = APIRouter(prefix="/piscinas", tags=["Piscinas"])
@router.post("/crear", response_model=PiscinaOutDTO, summary="Crear nueva piscina (solo admin)")
def crear_piscina(piscina: PiscinaCreateDTO, piscina_service: PiscinaService = Depends(get_piscina_service)):
    return piscina_service.crear_piscina(piscina)

@router.get("/lista", response_model=list[PiscinaOutDTO], summary="Listar todas las piscinas (solo admin)")
def listar_piscinas(piscina_service: PiscinaService = Depends(get_piscina_service)):
    return piscina_service.get_piscinas()

@router.get("/{piscina_id}", response_model=PiscinaOutDTO, summary="Obtener piscina por ID (solo admin)")
def obtener_piscina(piscina_id: int, piscina_service: PiscinaService = Depends(get_piscina_service)):
    return piscina_service.get_piscina_by_id(piscina_id)

@router.put("/actualizar/{piscina_id}", response_model=PiscinaOutDTO, summary="Actualizar piscina (solo admin)")
def actualizar_piscina(piscina_id: int, piscina: PiscinaUpdateDTO, piscina_service: PiscinaService = Depends(get_piscina_service)):
    return piscina_service.actualizar_piscina(piscina_id, piscina)

@router.delete("/borrar/{piscina_id}", summary="Eliminar piscina (solo admin)")
def eliminar_piscina(piscina_id: int, piscina_service: PiscinaService = Depends(get_piscina_service)):
    return piscina_service.eliminar_piscina(piscina_id)