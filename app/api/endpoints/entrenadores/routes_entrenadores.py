from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.entrenador import EntrenadorCreate, EntrenadorUpdate
from app.database import get_db
from app.crud import crud_entrenadores
from app.dependencies.admin import get_current_admin  

router = APIRouter(prefix="/entrenadores", tags=["Entrenadores"])

@router.post("/", summary="Crear nuevo entrenador (solo admin)")
def crear_entrenador(
    entrenador: EntrenadorCreate,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)  
):
    return crud_entrenadores.crear_entrenador(entrenador, db)

@router.get("/", summary="Listar todos los entrenadores (solo admin)")
def listar_entrenadores(
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_entrenadores.listar_entrenadores(db)

@router.get("/{entrenador_id}", summary="Obtener entrenador por ID (solo admin)")
def obtener_entrenador(
    entrenador_id: int,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    entrenador = crud_entrenadores.obtener_entrenador_por_id(entrenador_id, db)
    if entrenador is None:
        raise HTTPException(status_code=404, detail="Entrenador no encontrado")
    return entrenador

@router.put("/{entrenador_id}", summary="Actualizar enrtenador (solo admin)")
def actualizar_entrenador(
    entrenador_id: int,
    entrenador: EntrenadorUpdate,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_entrenadores.actualizar_entrenador(entrenador_id, entrenador, db)


@router.delete("/{entrenador_id}", summary="Eliminar entrenador (solo admin)")
def eliminar_entrenador(
    entrenador_id: int,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(get_current_admin)
):
    return crud_entrenadores.eliminar_entrenador(entrenador_id, db)