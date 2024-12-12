from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.bad_request_exception import BadRequestException


@dataclass(kw_only=True, slots=True)
class RequestForbiddenException(BadRequestException):
    error = BadRequestException.error + ".forbidden"

    detail: str = field(default="Forbidden")
    status_code: HTTPStatus = HTTPStatus.FORBIDDEN


__all__ = ("RequestForbiddenException",)
