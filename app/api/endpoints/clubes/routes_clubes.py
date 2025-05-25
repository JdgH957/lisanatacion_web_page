from fastapi import APIRouter, Depends
from app.application.DTOS.club_dto import ClubCreateDTO, ClubOutDTO, ClubUpdateDTO
from app.Domain.use_cases.club_service import ClubService
from app.config.dependencies.dependencies import get_club_service

router = APIRouter(prefix="/clubes", tags=["Clubes"])

@router.post("/crear", response_model=ClubOutDTO, summary="Crear nuevo club (solo admin)")
def crear_club(club: ClubCreateDTO, club_service: ClubService = Depends(get_club_service)):
    return club_service.crear_club(club)

@router.get("/lista", response_model=list[ClubOutDTO], summary="Listar todos los clubes (solo admin)")
def listar_clubes(club_service: ClubService = Depends(get_club_service)):
    return club_service.get_clubes()

@router.get("/{club_id}", response_model=ClubOutDTO, summary="Obtener club por ID (solo admin)")
def obtener_club(club_id: int, club_service: ClubService = Depends(get_club_service)):
    return club_service.get_club_by_id(club_id)

@router.put("/actualizar/{club_id}", response_model=ClubOutDTO, summary="Actualizar club (solo admin)")
def actualizar_club(club_id: int, club: ClubUpdateDTO, club_service: ClubService = Depends(get_club_service)):
    return club_service.actualizar_club(club_id, club)

@router.delete("/borrar/{club_id}", summary="Eliminar club (solo admin)")
def eliminar_club(club_id: int, club_service: ClubService = Depends(get_club_service)):
    return club_service.eliminar_club(club_id)