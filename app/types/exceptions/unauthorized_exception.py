from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.bad_request_exception import BadRequestException


@dataclass(kw_only=True, slots=True)
class UnauthorizedException(BadRequestException):
    error = BadRequestException.error + ".unauthorized"

    detail: str = field(default="Unauthorized")
    status_code: HTTPStatus = HTTPStatus.UNAUTHORIZED


__all__ = ("UnauthorizedException",)
