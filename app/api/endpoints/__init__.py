"""
Endpoints Module Initializer

This module initializes and aggregates the routes for the various
endpoints in the API. By importing all the endpoint routers here,
it simplifies the integration into the main FastAPI app instance.
"""
from fastapi import APIRouter
from app.api.endpoints import test_endpoints
from app.api.endpoints.usuarios import routes_usuarios
from app.api.endpoints.entrenadores import routes_entrenadores
from app.api.endpoints.admin import protegida
from app.api.endpoints.usuarios import auth_routes
# Create the router instance that will aggregate all the endpoint routers


ROUTER = APIRouter()

ROUTER.include_router(routes_usuarios.router)

ROUTER.include_router(routes_entrenadores.router)

ROUTER.include_router(protegida.router)

ROUTER.include_router(auth_routes.router)


# Ruta de test
ROUTER.include_router(
    test_endpoints.ROUTER,
    prefix="/api/v1",
    tags=["Test"]
)




