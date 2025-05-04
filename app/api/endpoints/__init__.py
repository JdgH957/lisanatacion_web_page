"""
Endpoints Module Initializer

This module initializes and aggregates the routes for the various
endpoints in the API. By importing all the endpoint routers here,
it simplifies the integration into the main FastAPI app instance.
"""
from fastapi import APIRouter
from fastapi import APIRouter
from app.api.endpoints import test_endpoints
from app.api.endpoints.usuarios import routes_usuarios

# Create the router instance that will aggregate all the endpoint routers
ROUTER = APIRouter()


ROUTER.include_router(
    test_endpoints.ROUTER,
    prefix = "/api/v1",
    tags = ["Test"]
    )

# Incluir el router de usuarios
ROUTER.include_router(
    routes_usuarios.router,
)