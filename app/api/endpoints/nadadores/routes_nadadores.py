from fastapi import APIRouter, Depends
from app.application.DTOS.nadador_dto import NadadorCreateDTO, NadadorOutDTO, NadadorUpdateDTO
from app.Domain.use_cases.nadador_service import NadadorService
from app.config.dependencies.dependencies import get_nadador_service


router = APIRouter(prefix="/nadadores", tags=["Nadadores"])

@router.post("/crear", response_model=NadadorOutDTO, summary="Crear nuevo nadador (solo admin)")
def crear_nadador(nadador: NadadorCreateDTO, nadador_service: NadadorService = Depends(get_nadador_service)):
    return nadador_service.crear_nadador(nadador)

@router.get("/lista", response_model=list[NadadorOutDTO], summary="Listar todos los nadadores (solo admin)")
def listar_nadadores(nadador_service: NadadorService = Depends(get_nadador_service)):
    return nadador_service.get_nadadores()

@router.get("/{nadador_id}", response_model=NadadorOutDTO, summary="Obtener nadador por ID (solo admin)")
def obtener_nadador(nadador_id: int, nadador_service: NadadorService = Depends(get_nadador_service)):
    return nadador_service.get_nadador_by_id(nadador_id)

@router.put("/actualizar/{nadador_id}", response_model=NadadorOutDTO, summary="Actualizar nadador (solo admin)")
def actualizar_nadador(nadador_id: int, nadador: NadadorUpdateDTO, nadador_service: NadadorService = Depends(get_nadador_service)):
    return nadador_service.actualizar_nadador(nadador_id, nadador)

@router.delete("/borrar/{nadador_id}", summary="Eliminar nadador (solo admin)")
def eliminar_nadador(nadador_id: int, nadador_service: NadadorService = Depends(get_nadador_service)):
    return nadador_service.eliminar_nadador(nadador_id)
