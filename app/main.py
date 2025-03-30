"""
Main Application Module

This module initializes the FastAPI application, configures the OpenAI API settings,
sets up the error-handling middleware, and includes the main application router.

Attributes:
    app (FastAPI): Instance of the FastAPI application.
    openai.api_type (str): Type of OpenAI API being used.
    openai.api_base (str): Base URL for the OpenAI API.
    openai.api_version (str): Version of the OpenAI API being used.
    openai.api_key (str): API key for accessing the OpenAI API.
"""
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import Response
from app.api.endpoints import ROUTER
from app.core.error_handlers import register_exception_handlers

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Usuario, Club
from datetime import datetime



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
    try:
        fecha_asignacion = datetime.strptime(fecha_asig, "%Y-%m-%d")  # Convierte el string a datetime
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha incorrecto, usa YYYY-MM-DD")

    usuario = Usuario(nombre=nombre, contra=contra, email=email, fecha_asig=fecha_asignacion, rol=rol)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return {"message": "✅ Usuario creado", "usuario": usuario}


# 🚀 Endpoint para listar usuarios
@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

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

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "*"
        ],    # Lista de orígenes permitidos, ajusta según sea necesario
    allow_credentials = True,
    allow_methods = ["*"],    # Métodos HTTP permitidos
    allow_headers = ["*"],    # Encabezados HTTP permitidos
    )

# Register the error-handling middleware
register_exception_handlers(app)

# Include the router in the application
app.include_router(ROUTER)

app.mount(
    "/static",
    StaticFiles(
        directory = Path(__file__).parent.parent.absolute() /
        "app/templates/static"
        ),
    name = "static",
    )


templates = Jinja2Templates(directory = "app/templates")

@app.get("/", response_class = HTMLResponse)    # type: ignore
def index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})