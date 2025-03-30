from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Usuario, Club

app = FastAPI()

# Función para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🚀 Endpoint para crear un usuario
@app.post("/usuarios/")
def crear_usuario(nombre: str, contra: str, email: str, fecha_asig: str, rol: str, db: Session = Depends(get_db)):
    usuario = Usuario(nombre=nombre, contra=contra, email=email, fecha_asig=fecha_asig, rol=rol)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"message": "✅ Usuario creado", "usuario": usuario}

# 🚀 Endpoint para listar usuarios
@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

# 🚀 Endpoint para crear un club y asociar entrenadores
@app.post("/clubes/")
def crear_club(nombre: str, entrenadores_ids: list[int], db: Session = Depends(get_db)):
    entrenadores = db.query(Usuario).filter(Usuario.id.in_(entrenadores_ids), Usuario.rol == "entrenador").all()
    if not entrenadores:
        raise HTTPException(status_code=400, detail="No se encontraron entrenadores válidos")

    club = Club(nombre=nombre, entrenadores=entrenadores)
    db.add(club)
    db.commit()
    db.refresh(club)
    return {"message": f"✅ Club '{nombre}' creado", "club": club}

# 🚀 Endpoint para listar clubes y sus entrenadores
@app.get("/clubes/")
def listar_clubes(db: Session = Depends(get_db)):
    clubes = db.query(Club).all()
    return [{"id": c.id, "nombre": c.nombre, "entrenadores": [{"id": e.id, "nombre": e.nombre} for e in c.entrenadores]} for c in clubes]
