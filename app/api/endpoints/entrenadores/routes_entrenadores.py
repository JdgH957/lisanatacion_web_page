from fastapi import APIRouter, Depends, HTTPException
from app.application.DTOS.entrenador_dto import EntrenadorCreateDTO, EntrenadorOutDTO, EntrenadorUpdateDTO
from app.Domain.use_cases.entrenador_service import EntrenadorService
from app.config.dependencies.dependencies import get_entrenador_service
from app.core.auth.jwt_bearer import JwtBearer

router = APIRouter(prefix="/entrenadores", tags=["Entrenadores"])

@router.post("/crear", response_model=EntrenadorOutDTO, summary="Crear nuevo entrenador (solo admin)")
def crear_entrenador(
    entrenador: EntrenadorCreateDTO,
    entrenador_service: EntrenadorService = Depends(get_entrenador_service),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return entrenador_service.crear_entrenador(entrenador)


@router.get("/lista", response_model=list[EntrenadorOutDTO], summary="Listar todos los entrenadores (solo admin)")
def listar_entrenadores(
    entrenador_service: EntrenadorService = Depends(get_entrenador_service),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return entrenador_service.get_entrenadores()


@router.get("/{entrenador_id}", response_model=EntrenadorOutDTO, summary="Obtener entrenador por ID (solo admin)")
def obtener_entrenador(
    entrenador_id: int,
    entrenador_service: EntrenadorService = Depends(get_entrenador_service),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return entrenador_service.get_entrenador_by_id(entrenador_id)


@router.put("/actualizar/{entrenador_id}", response_model=EntrenadorOutDTO, summary="Actualizar entrenador (solo admin)")
def actualizar_entrenador(
    entrenador_id: int,
    entrenador: EntrenadorUpdateDTO,
    entrenador_service: EntrenadorService = Depends(get_entrenador_service),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return entrenador_service.actualizar_entrenador(entrenador_id, entrenador)


@router.delete("/borrar/{entrenador_id}", summary="Eliminar entrenador (solo admin)")
def eliminar_entrenador(
    entrenador_id: int,
    entrenador_service: EntrenadorService = Depends(get_entrenador_service),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    return entrenador_service.eliminar_entrenador(entrenador_id)
