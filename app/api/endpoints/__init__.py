"""
Endpoints Module Initializer

This module initializes and aggregates the routes for the various
endpoints in the API. By importing all the endpoint routers here,
it simplifies the integration into the main FastAPI app instance.
"""
from fastapi import APIRouter
# Import the routers for the specific functionalities
from . import (
    test_endpoints
    )

# Create the router instance that will aggregate all the endpoint routers
ROUTER = APIRouter()


ROUTER.include_router(
    test_endpoints.ROUTER,
    prefix = "/api/v1",
    tags = ["Test"]
    )