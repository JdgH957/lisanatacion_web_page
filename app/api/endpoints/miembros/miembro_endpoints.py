# app/api/endpoints/miembros/miembro_endpoints.py

import json
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import urllib.parse
from app.database import get_db
from app.infrastructure.db.DBModels.curso_orm import CursoORM
from app.infrastructure.db.DBModels.miembro_orm import MiembroORM
from app.application.DTOS.miembro_dto import InscripcionMiembroRequest, MiembroCreateDTO, MiembroOutDTO, MiembroUpdateDTO
from app.core.auth.jwt_bearer import JwtBearer
from app.services.pay_services import crear_link_pago_miembro

router = APIRouter(prefix="/miembros", tags=["Miembros"])


@router.get("/postpago")
def post_pago_miembro(request: Request, db: Session = Depends(get_db)):
    estado = request.query_params.get("estado")
    external_reference = request.query_params.get("external_reference")
    """
    if estado != "success" or not external_reference:
        return RedirectResponse(url="https://www.google.com?error=fallido")"""

    try:
        decoded = urllib.parse.unquote(external_reference)
        data = json.loads(decoded)

        nuevo_miembro = MiembroORM(
            nombre=data["nombre"],
            edad=data["edad"],
            curso_id=data["curso_id"],
            tipo_miembro=data["tipo_miembro"],
            estado_pago="pagado"
        )

        db.add(nuevo_miembro)

        curso = db.query(CursoORM).filter(CursoORM.id_curso == data["curso_id"]).first()
        if curso:
            curso.cantidad_miembros += 1

        db.commit()

    except Exception as e:
        return RedirectResponse(url="https://www.google.com?error=procesamiento")

    return RedirectResponse(url="https://www.google.com?estado=exito")


@router.post("/crear", response_model=MiembroOutDTO)
def crear_miembro(
    data: MiembroCreateDTO,
    db: Session = Depends(get_db),
    token: dict = Depends(JwtBearer())
):
    nuevo = MiembroORM(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/lista", response_model=list[MiembroOutDTO])
def listar_miembros(db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    return db.query(MiembroORM).all()

@router.get("/{miembro_id}", response_model=MiembroOutDTO)
def obtener_miembro(miembro_id: int, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    miembro = db.query(MiembroORM).filter(MiembroORM.id_miembro == miembro_id).first()
    if not miembro:
        raise HTTPException(status_code=404, detail="Miembro no encontrado")
    return miembro

@router.put("/actualizar/{miembro_id}", response_model=MiembroOutDTO)
def actualizar_miembro(miembro_id: int, data: MiembroUpdateDTO, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    miembro = db.query(MiembroORM).filter(MiembroORM.id_miembro == miembro_id).first()
    if not miembro:
        raise HTTPException(status_code=404, detail="Miembro no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(miembro, key, value)
    db.commit()
    db.refresh(miembro)
    return miembro

@router.delete("/borrar/{miembro_id}")
def eliminar_miembro(miembro_id: int, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    miembro = db.query(MiembroORM).filter(MiembroORM.id_miembro == miembro_id).first()
    if not miembro:
        raise HTTPException(status_code=404, detail="Miembro no encontrado")
    db.delete(miembro)
    db.commit()
    return {"message": "Miembro eliminado correctamente"}


@router.post("/crear-pago")
def crear_pago_miembro(
    data: InscripcionMiembroRequest,
    db: Session = Depends(get_db),
    token: dict = Depends(JwtBearer())
):
    link = crear_link_pago_miembro(data, db)
    return {"link_de_pago": link}
