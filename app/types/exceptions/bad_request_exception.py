from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.base import APIException


@dataclass(kw_only=True, slots=True)
class BadRequestException(APIException):
    error = "bad_request"

    detail: str = field(default="Bad Request")
    status_code: HTTPStatus = HTTPStatus.BAD_REQUEST


__all__ = ("BadRequestException",)
