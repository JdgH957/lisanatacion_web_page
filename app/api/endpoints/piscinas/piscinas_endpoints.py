from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.auth.jwt_bearer import JwtBearer
from app.infrastructure.db.DBModels.piscina_orm import PiscinaORM
from app.application.DTOS.piscina_dto import PiscinaCreateDTO, PiscinaOutDTO, PiscinaUpdateDTO

router = APIRouter(prefix="/piscinas", tags=["Piscinas"])

@router.post("/crear", response_model=PiscinaOutDTO)
def crear_piscina(
    piscina_data: PiscinaCreateDTO,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())  # valida y decodifica el JWT
):
    nueva_piscina = PiscinaORM(
        aforo_maximo=piscina_data.aforo_maximo,
        profundidad=piscina_data.profundidad,
        tipo_piscina=piscina_data.tipo_piscina,
        largo=piscina_data.largo,
        ancho=piscina_data.ancho
    )

    db.add(nueva_piscina)
    db.commit()
    db.refresh(nueva_piscina)

    return nueva_piscina


@router.get("/lista", response_model=list[PiscinaOutDTO], summary="Listar todas las piscinas (solo admin)")
def listar_piscinas(db: Session = Depends(get_db), token_data: dict = Depends(JwtBearer())):
    piscinas = db.query(PiscinaORM).all()
    return piscinas

@router.get("/{piscina_id}", response_model=PiscinaOutDTO, summary="Obtener piscina por ID (solo admin)")
def obtener_piscina(piscina_id: int, db: Session = Depends(get_db), token_data: dict = Depends(JwtBearer())):
    piscina = db.query(PiscinaORM).filter(PiscinaORM.id_piscina == piscina_id).first()
    if not piscina:
        raise HTTPException(status_code=404, detail="Piscina no encontrada")
    return piscina

@router.delete("/borrar/{piscina_id}", summary="Eliminar piscina (solo admin)")
def eliminar_piscina(piscina_id: int, db: Session = Depends(get_db), token_data: dict = Depends(JwtBearer())):
    piscina = db.query(PiscinaORM).filter(PiscinaORM.id_piscina == piscina_id).first()
    if not piscina:
        raise HTTPException(status_code=404, detail="Piscina no encontrada")

    db.delete(piscina)
    db.commit()
    return {"message": "Piscina eliminada correctamente"}
