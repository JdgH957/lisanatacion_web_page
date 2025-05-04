"""
Exception Handling Registration for a FastAPI Application.

This module offers a streamlined mechanism for registering both custom and default
exception handlers for a FastAPI application. By associating specific exception types
with corresponding handlers, it ensures that FastAPI appropriately delegates error
handling when such exceptions arise during request processing. This results in
consistent error responses and standardized logging practices.

Exceptions Handled:
- `RequestValidationError`: Handles request validation errors.
- `DatabaseError`: Custom exception for issues related to the database.
- `ExternalAPIError`: Custom exception for errors arising from external API interactions.
- `CustomTokenError`: Custom exception addressing JWT token-related anomalies.
- `BadRequestError`: Custom exception for handling bad requests.
- `NotFoundError`: Custom exception for scenarios where a requested resource isn't found.
- `UnprocessableEntityError`: Custom exception for cases where the entity cannot be processed.
- `UnauthorizedError`: Custom exception indicating unauthorized access attempts.
- `HTTPException`: Tackles generic HTTP exceptions.
- `Exception`: A general handler for exceptions that don't match other specified handlers.
"""

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler
from app.core.error_handlers.custom_exceptions import (
    BadRequestError,
    ConflictError,
    CustomTokenError,
    DatabaseError,
    ExternalAPIError,
    NotFoundError,
    SelfRegistrationBlockedError,
    UnauthorizedError,
    UnexpectedError,
    UnprocessableEntityError,
    TimeoutAPIError,
    )
from app.core.error_handlers.error_handlers import (
    bad_request_exception_handler,
    conflict_exception_handler,
    custom_token_exception_handler,
    database_exception_handler,
    external_api_exception_handler,
    self_registration_exception_handler,
    unexpected_exception_handler,
    not_found_exception_handler,
    unauthorized_exception_handler,
    unprocessable_entity_exception_handler,
    validation_exception_handler,
    timeout_api_exception_handler,
    )


def register_exception_handlers(app: FastAPI) -> None:
    """
    Registers custom and default exception handlers to a FastAPI application.

    This function sets up associations between exception types and their corresponding
    handlers for a given FastAPI application. By doing so, it ensures that when an
    exception is raised, the app delegates the error handling to the appropriate handler,
    leading to consistent and informative error responses.

    Args:
        app: The FastAPI application instance to which the exception handlers are registered.

    Usage:
        Typically used during the initialization or setup phase of a FastAPI application.
    """

    app.exception_handler(RequestValidationError)(validation_exception_handler)
    app.exception_handler(DatabaseError)(database_exception_handler)
    app.exception_handler(ExternalAPIError)(external_api_exception_handler)
    app.exception_handler(CustomTokenError)(custom_token_exception_handler)
    app.exception_handler(NotFoundError)(not_found_exception_handler)
    app.exception_handler(BadRequestError)(bad_request_exception_handler)
    app.exception_handler(UnprocessableEntityError
                          )(unprocessable_entity_exception_handler)
    app.exception_handler(UnauthorizedError)(unauthorized_exception_handler)
    app.exception_handler(ConflictError)(conflict_exception_handler)
    app.exception_handler(HTTPException)(http_exception_handler)
    app.exception_handler(UnexpectedError)(unexpected_exception_handler)
    app.exception_handler(Exception)(unexpected_exception_handler)
    app.exception_handler(TimeoutAPIError)(timeout_api_exception_handler)
    app.exception_handler(SelfRegistrationBlockedError
                          )(self_registration_exception_handler)
