from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.infrastructure.db.DBModels.horario_orm import HorarioORM
from app.application.DTOS.horario_dto import HorarioCreateDTO, HorarioFiltroDTO, HorarioOutDTO, ReservaHorariosCursoNuevoRequest
from app.core.auth.jwt_bearer import JwtBearer
from app.services.pay_services import crear_link_de_pago_reserva

router = APIRouter(prefix="/horarios", tags=["Horarios"])

@router.post("/crear", response_model=HorarioOutDTO)
def crear_horario(
    horario_data: HorarioCreateDTO,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")

    nuevo_horario = HorarioORM(**horario_data.dict())
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario


@router.get("/lista", response_model=list[HorarioOutDTO])
def listar_horarios(
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):

    return db.query(HorarioORM).all()


@router.get("/{horario_id}", response_model=HorarioOutDTO)
def obtener_horario(
    horario_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):

    horario = db.query(HorarioORM).filter(HorarioORM.id_horario == horario_id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario


@router.delete("/borrar/{horario_id}")
def eliminar_horario(
    horario_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):
    if token_data["rol"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")

    horario = db.query(HorarioORM).filter(HorarioORM.id_horario == horario_id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")

    db.delete(horario)
    db.commit()
    return {"message": "Horario eliminado correctamente"}


@router.get("/por-piscina/{piscina_id}", response_model=list[HorarioOutDTO], summary="Listar horarios por piscina")
def listar_horarios_por_piscina(
    piscina_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):
    horarios = db.query(HorarioORM).filter(
        HorarioORM.piscina_id == piscina_id,
        HorarioORM.disponible == True
    ).all()
    return horarios


@router.post("/filtrar-body", response_model=list[HorarioOutDTO])
def filtrar_horarios_body(
    filtro: HorarioFiltroDTO,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JwtBearer())
):

    horarios = db.query(HorarioORM).filter(
        HorarioORM.piscina_id == filtro.piscina_id,
        HorarioORM.dia == filtro.dia.value,
        HorarioORM.mes == filtro.mes.value,
        HorarioORM.disponible == True
    ).all()

    return horarios


@router.post("/crear-pago/curso/nuevo")
def crear_pago_para_horarios_curso_nuevo(
    data: ReservaHorariosCursoNuevoRequest,
    db: Session = Depends(get_db),
    token: dict = Depends(JwtBearer())
):
    link = crear_link_de_pago_reserva(data, db=db)
    return {"link_de_pago": link}


