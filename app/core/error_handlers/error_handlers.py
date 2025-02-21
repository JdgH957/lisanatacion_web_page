"""
Error Handling Module for FastAPI application.

This module provides enhanced error handlers for various types of exceptions that may arise
during the execution of the application. Each error handler enriches the HTTP response
with additional information about the request and the full error details.

The module defines handlers for:
- ValidationError: Raised when input data validation fails.
- DatabaseError: Raised for errors related to database operations.
- ExternalAPIError: Raised when external APIs return errors.
- HTTPException: Raised for standard HTTP errors.
- Exception: General catch-all handler for unexpected errors.

Usage:
    from error_handlers import validation_exception_handler, database_exception_handler

    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(DatabaseError, database_exception_handler)

Dependencies:
    - fastapi
    - custom_exceptions module for application-specific exceptions.
"""

from typing import Any, Dict
from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.config import APP_LOGGER
from app.core.error_handlers.custom_exceptions import (
    BadRequestError, ConflictError, CustomTokenError, DatabaseError,
    NotFoundError, SelfRegistrationBlockedError, UnauthorizedError,
    ExternalAPIError, UnexpectedError, UnprocessableEntityError,
    TimeoutAPIError
    )


def enrich_response(
        request: Request, detail: str, error: str | list[str], status_code: int
    ) -> Dict[str, Any]:
    """
    Enriches the response with additional error information.

    Args:
        request (Request): The request object.
        detail (str): The error detail.
        error (CustomBaseError): The custom error object.
        status_code (int): The HTTP status code.

    Returns:
        dict[str, Any]: The enriched response dictionary.
    """
    APP_LOGGER.error('Error: %s, Detail: %s', error, detail)
    return {
        "detail": detail,
        "error": error,
        "status_code": status_code,
        "request":
            {
                "path": request.url.path,    # type: ignore
                "method": request.method,
                "query_params": dict(request.query_params)
                }
        }


async def custom_token_exception_handler(
        request: Request, exc: CustomTokenError
    ) -> JSONResponse:
    """
    Handle `CustomTokenError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of the token error.

    Args:
        request (Request): The request that caused the error.
        exc (CustomTokenError): The raised custom token exception.

    Returns:
        JSONResponse: A JSON response with a status code of 400 (Bad Request),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "CustomTokenError -  An error creating a token occurred.",
        f"CustomTokenError: {exc}",
        status_code = 400
        )
    return JSONResponse(status_code = 400, content = content)


async def bad_request_exception_handler(
        request: Request, exc: BadRequestError
    ) -> JSONResponse:
    """
    Handle `BadRequestError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of the error in the request.

    Args:
        request (Request): The request that caused the error.
        exc (CustomTokenError): The raised custom token exception.

    Returns:
        JSONResponse: A JSON response with a status code of 400 (Bad Request),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "BadRequestError -  An error occurred.",
        f"Bad request: {exc}",
        status_code = 400
        )
    return JSONResponse(status_code = 400, content = content)


async def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedError,
    ) -> JSONResponse:
    """
    Handle `UnauthorizedError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of the issue with credentials.

    Args:
        request (Request): The request that caused the error.
        exc (UnauthorizedError): The raised unauthorized exception.

    Returns:
        JSONResponse: A JSON response with a status code of 401 (Unauthorized),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "UnauthorizedError -  A credentials error occurred.",
        f"Unauthorized: {exc}",
        status_code = 401
        )
    return JSONResponse(status_code = 401, content = content)


async def self_registration_exception_handler(
    request: Request,
    exc: SelfRegistrationBlockedError,
    ) -> JSONResponse:
    """
    Handles exceptions of type SelfRegistrationBlockedError by returning a JSON response
    with a status code of 423 (Locked).

    Args:
        request (Request): The incoming HTTP request.
        exc (SelfRegistrationBlockedError): The exception instance that was raised.

    Returns:
        JSONResponse: A JSON response containing the error details and a status code of 423.
    """
    content = enrich_response(
        request,
        "SelfRegistrationError - Self-registration has been blocked for this client.",
        f"Self registration blocked: {exc}",
        status_code = 423
        )
    return JSONResponse(status_code = 423, content = content)


async def conflict_exception_handler(
        request: Request, exc: ConflictError
    ) -> JSONResponse:
    """
    Handle `ConflictError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of the issue with credentials.

    Args:
        request (Request): The request that caused the error.
        exc (ConflictError): The raised conflict exception.

    Returns:
        JSONResponse: A JSON response with a status code of 409 (Conflict),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "ConflictError -  A credentials error occurred.",
        f"Conflict: {exc}",
        status_code = 409
        )
    return JSONResponse(status_code = 409, content = content)


async def not_found_exception_handler(
        request: Request, exc: NotFoundError
    ) -> JSONResponse:
    """
    Handle `NotFoundError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of whatever the system could not find.

    Args:
        request (Request): The request that caused the error.
        exc (NotFoundError): The raised notfound exception.

    Returns:
        JSONResponse: A JSON response with a status code of 404 (Not found),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "NotFoundError -  The entity was not found.",
        f"Not found: {exc}",
        status_code = 404
        )
    return JSONResponse(status_code = 404, content = content)


async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
    """
    Handle `RequestValidationError` exceptions.

    Enriches the HTTP response with information about the request and details of the error.

    Args:
        request (Request): The request that caused the error.
        exc (RequestValidationError): The raised validation exception.

    Returns:
        JSONResponse: A JSON response with a status code of 422,
                      and detailed error information.
    """
    error_msgs = [
        f"{error['loc'][1]}: {error['msg']}" for error in exc.errors()
        ]

    content = enrich_response(
        request,
        "An error validating input data occurred.",
        error_msgs,
        status_code = 422
        )
    return JSONResponse(status_code = 422, content = content)


async def unprocessable_entity_exception_handler(
        request: Request, exc: UnprocessableEntityError
    ) -> JSONResponse:
    """
    Handle `UnprocessableEntityError` exceptions.
    """
    content = enrich_response(
        request,
        "UnprocessableEntityError - An entity was unprocessable.",
        f"Unprocessable Entity: {exc}",
        status_code = 422
        )
    return JSONResponse(status_code = 422, content = content)


async def unexpected_exception_handler(
        request: Request, exc: UnexpectedError
    ) -> JSONResponse:
    """
    Handle general unexpected exceptions.

    Enriches the HTTP response with information about the request,
    and a generic error message.

    Args:
        request (Request): The request that caused the error.
        exc (Exception): The raised generic exception.

    Returns:
        JSONResponse: A JSON response with a status code of 500 (Internal Server Error),
                      and a generic error message.
    """
    content = enrich_response(
        request,
        "Unexpected Error -  An unexpected error occurred.",
        f"Unexpected Error: {exc}",
        status_code = 500
        )
    return JSONResponse(status_code = 500, content = content)


async def database_exception_handler(
        request: Request, exc: DatabaseError
    ) -> JSONResponse:
    """
    Handle database-related exceptions.

    Enriches the HTTP response with information about the request,
    and a generic database error message.

    Args:
        request (Request): The request that caused the error.

    Returns:
        JSONResponse: A JSON response with a status code of 500 (Internal Server Error),
        and a generic database error message.
    """
    content = enrich_response(
        request,
        "Database Error -  A database error occurred.",
        f"Database Error: {exc}",
        status_code = 500
        )
    return JSONResponse(status_code = 500, content = content)


async def external_api_exception_handler(
        request: Request, exc: ExternalAPIError
    ) -> JSONResponse:
    """
    Handle `ExternalAPIError` exceptions.

    Enriches the HTTP response with information about the request,
    and details of the external API error.

    Args:
        request (Request): The request that caused the error.
        exc (ExternalAPIError): The raised external API exception.

    Returns:
        JSONResponse: A JSON response with a status code of 502 (Bad Gateway),
        and detailed error information.
    """
    content = enrich_response(
        request,
        "External API Error - An external API error occurred.",
        f"External API Error: {exc}",
        status_code = 502
        )

    return JSONResponse(status_code = 502, content = content)


async def http_exception_handler(
        request: Request, exc: HTTPException
    ) -> JSONResponse:
    """
    Handle standard `HTTPException` errors.

    Enriches the HTTP response with information about the request,
    and details of the HTTP error.

    Args:
        request (Request): The request that caused the error.
        exc (HTTPException): The raised HTTP exception.

    Returns:
        JSONResponse: A JSON response with a status code matching the HTTPException's status code
                      and detailed error information.
    """

    content = enrich_response(
        request,
        exc.detail,
        f"HTTP Exception: {exc.detail}",
        status_code = exc.status_code
        )
    return JSONResponse(status_code = exc.status_code, content = content)


async def timeout_api_exception_handler(
        request: Request, exc: TimeoutAPIError
    ) -> JSONResponse:
    """
    Handles a timeout API error and returns a JSON response with the appropriate content.

    Args:
        request (Request): The incoming request object.
        exc (TimeoutAPIError): The timeout API error that occurred.

    Returns:
        JSONResponse: The JSON response with the error content and status code 408.
    """
    content = enrich_response(
        request,
        "Timeout API Error -  An timeout API error occurred.",
        f"Timeout API Error: {exc}",
        status_code = 408
        )

    return JSONResponse(status_code=408, content=content)
