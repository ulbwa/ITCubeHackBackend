from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.internal_server_exception import InternalServerException


@dataclass(kw_only=True, slots=True)
class ServiceUnavailableException(InternalServerException):
    error = InternalServerException.error + ".service_unavailable"

    detail: str = field(default="Service Unavailable")
    status_code: HTTPStatus = HTTPStatus.SERVICE_UNAVAILABLE


__all__ = ("ServiceUnavailableException",)
