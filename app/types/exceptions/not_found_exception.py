from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.bad_request_exception import BadRequestException


@dataclass(kw_only=True, slots=True)
class NotFoundException(BadRequestException):
    error = BadRequestException.error + ".not_found"

    detail: str = field(default="Not Found")
    status_code: HTTPStatus = HTTPStatus.NOT_FOUND


__all__ = ("NotFoundException",)
