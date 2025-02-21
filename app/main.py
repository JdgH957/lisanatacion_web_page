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
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware    # To delete after implement proper frontend
from app.api.endpoints import ROUTER
from app.core.error_handlers import register_exception_handlers


app = FastAPI()

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
