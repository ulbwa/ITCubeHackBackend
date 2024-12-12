from http import HTTPStatus
from logging import getLogger
from typing import Any

from litestar import Request, Response
from litestar.exceptions import (
    HTTPException,
    ImproperlyConfiguredException,
    InternalServerException,
    MethodNotAllowedException,
    NoRouteMatchFoundException,
    NotAuthorizedException,
    NotFoundException,
    PermissionDeniedException,
    ServiceUnavailableException,
    TemplateNotFoundException,
    TooManyRequestsException,
    ValidationException,
)
from litestar.types import ExceptionHandlersMap

from app.types import exceptions

logger = getLogger("exception-handler")


def create_exception_response(exception: exceptions.APIException) -> Response:
    content: dict[str, Any] = dict(detail=exception.detail)
    response = Response(content, status_code=exception.status_code)
    if exception.headers:
        response.headers.update(exception.headers)
    response.headers.update({"X-Error": exception.error})  # TODO: use value from config
    return response


def service_exception_handler(
    request: Request, exception: exceptions.APIException
) -> Response:
    return create_exception_response(exception)


def validation_exception_handler(
    request: Request, exception: ValidationException
) -> Response:
    return create_exception_response(
        exceptions.RequestForbiddenException(detail="Validation Error")
    )


def litestar_exception_handler(request: Request, exception: HTTPException) -> Response:
    mapping = {
        NotAuthorizedException: exceptions.UnauthorizedException,
        PermissionDeniedException: exceptions.RequestForbiddenException,
        NotFoundException: exceptions.NotFoundException,
        MethodNotAllowedException: exceptions.MethodNotAllowedException,
        TooManyRequestsException: exceptions.TooManyRequestsException,
        InternalServerException: exceptions.InternalServerException,
        ServiceUnavailableException: exceptions.ServiceUnavailableException,
        NoRouteMatchFoundException: exceptions.InternalServerException,
        TemplateNotFoundException: exceptions.InternalServerException,
        ImproperlyConfiguredException: exceptions.InternalServerException,
    }

    if exc_cls := mapping.get(type(exception)):  # type: ignore
        return create_exception_response(
            exc_cls(detail=exception.detail, headers=exception.headers)
        )

    logger.warning("Unhandled Litestar Exception", exc_info=exception)

    return create_exception_response(
        exceptions.InternalServerException(
            status_code=HTTPStatus(exception.status_code),
            detail=exception.detail,
            headers=exception.headers,
        )
    )


def internal_exception_handler(request: Request, exception: Exception) -> Response:
    logger.exception(None, exc_info=exception)
    return create_exception_response(exceptions.InternalServerException())


def get_exception_handlers() -> ExceptionHandlersMap:
    return {  # type: ignore
        exceptions.APIException: service_exception_handler,
        ValidationException: validation_exception_handler,
        HTTPException: litestar_exception_handler,
        Exception: internal_exception_handler,
    }


__all__ = ("get_exception_handlers",)
