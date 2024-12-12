from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.base import APIException


@dataclass(kw_only=True, slots=True)
class InternalServerException(APIException):
    error = "internal"

    detail: str = field(default="Internal Server Error")
    status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR


__all__ = ("InternalServerException",)
