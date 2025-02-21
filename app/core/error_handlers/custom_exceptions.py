"""
Custom Exceptions Module for FastAPI application.

This module defines the custom exceptions that can be raised throughout the application.
These exceptions are tailored to specific error scenarios, improving error handling and
reporting capabilities.

Usage:
    from custom_exceptions import ValidationError, DatabaseError, ExternalAPIError
    if condition:
        raise ValidationError("Specific validation message")
"""


from typing import Any, Dict


class CustomBaseError(Exception):
    """Base for all custom errors."""

    def __init__(
            self, message: str, details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message)
        self.details = details

    def __str__(self) -> str:
        base_message = super().__str__()
        if self.details:
            return f"{base_message}. Details: {self.details}"
        return base_message


class CustomTokenError(CustomBaseError):
    """Raised when there is an error creating or decoding a JWT token."""

    def __init__(
            self,
            message: str = "Token error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class NotFoundError(CustomBaseError):
    """Raised when an entity is not found in the database."""

    def __init__(
            self,
            message: str = "Not found",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class BadRequestError(CustomBaseError):
    """Raised when there is an error processing data in an endpoint."""

    def __init__(
            self,
            message: str = "Bad request",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class UnprocessableEntityError(CustomBaseError):
    """Validation error, such as when request parameters are incorrect."""

    def __init__(
            self,
            message: str = "Unprocessable Entity",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class UnauthorizedError(CustomBaseError):
    """Error related to unauthorized access."""

    def __init__(
            self,
            message: str = "Unauthorized",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class SelfRegistrationBlockedError(CustomBaseError):
    """Error related to blocking user self-registration."""

    def __init__(
            self,
            message: str = "Self registration blocked",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class ConflictError(CustomBaseError):
    """Error related to conflicts."""

    def __init__(
            self,
            message: str = "Conflict",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class UnexpectedError(CustomBaseError):
    """Error related to unexpected errors"""

    def __init__(
            self,
            message: str = "Unexpected error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class DatabaseError(CustomBaseError):
    """Error related to database operations."""

    def __init__(
            self,
            message: str = "Database error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message)


class ExternalAPIError(CustomBaseError):
    """Error when communicating with an external API or when an external API returns an error."""

    def __init__(
            self,
            message: str = "External API error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class FileNotFoundSVEAPIError(CustomBaseError):
    """Error consuming the SVE API to download the latest version of a document and the file is not found."""

    def __init__(
            self,
            message: str = "File Not Found SVE API Error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class IOExceptionSVEAPIError(CustomBaseError):
    """Error creating document file with HTML template."""

    def __init__(
            self,
            message: str = "IO Exception HTML SVE API Error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)


class TimeoutAPIError(CustomBaseError):
    """Error when communicating with an external API or when an external API does not respond within a certain time."""

    def __init__(
            self,
            message: str = "Timeout API error",
            details: Dict[Any, Any] | None = None
        ) -> None:
        super().__init__(message, details)
