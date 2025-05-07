from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.crud import crud_usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", summary="Crear nuevo usuario")
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crud_usuarios.crear_usuario(usuario, db)
#error
@router.get("/", summary="Listar todos los usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    return crud_usuarios.listar_usuarios(db)

@router.get("/{usuario_id}", summary="Obtener usuario por ID")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuarios.obtener_usuario_por_id(usuario_id, db)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", summary="Actualizar usuario")
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    return crud_usuarios.actualizar_usuario(usuario_id, usuario, db)

@router.delete("/{usuario_id}", summary="Eliminar usuario")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return crud_usuarios.eliminar_usuario(usuario_id, db)
