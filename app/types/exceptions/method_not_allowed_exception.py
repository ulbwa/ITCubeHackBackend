from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.bad_request_exception import BadRequestException


@dataclass(kw_only=True, slots=True)
class MethodNotAllowedException(BadRequestException):
    error = BadRequestException.error + ".method_not_allowed"

    detail: str = field(default="Method Not Allowed")
    status_code: HTTPStatus = HTTPStatus.METHOD_NOT_ALLOWED


__all__ = ("MethodNotAllowedException",)
