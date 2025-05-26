from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.auth.jwt_bearer import JwtBearer
from app.infrastructure.db.DBModels.curso_orm import CursoORM
from app.application.DTOS.curso_dto import CursoCreateDTO, CursoOutDTO
from app.services.pay_services import procesar_postpago_curso

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.get("/postpago")
def post_pago_curso(request: Request, db: Session = Depends(get_db)):
    print("Procesando postpago curso")
    estado = request.query_params.get("estado")
    payment_id = request.query_params.get("payment_id")
    external_reference = request.query_params.get("external_reference")

    if not payment_id or not external_reference:
        return RedirectResponse(url="https://www.google.com=sin_datos")

    resultado = procesar_postpago_curso(payment_id, external_reference, db)
    return RedirectResponse(url=f"https://www.google.com={resultado}")


@router.get("/debug")
def debug_simple():
    print("✅ Entró al endpoint más simple")
    return {"mensaje": "Este endpoint funciona"}


@router.post("/crear", response_model=CursoOutDTO)
def crear_curso(data: CursoCreateDTO, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    nuevo_curso = CursoORM(**data.dict(), cantidad_miembros=0)
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

@router.get("/lista", response_model=list[CursoOutDTO])
def listar_cursos(db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    return db.query(CursoORM).all()

@router.get("/{curso_id}", response_model=CursoOutDTO)
def obtener_curso(curso_id: int, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    curso = db.query(CursoORM).filter(CursoORM.id_curso == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

@router.delete("/borrar/{curso_id}")
def eliminar_curso(curso_id: int, db: Session = Depends(get_db), token: dict = Depends(JwtBearer())):
    curso = db.query(CursoORM).filter(CursoORM.id_curso == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    db.delete(curso)
    db.commit()
    return {"message": "Curso eliminado correctamente"}

