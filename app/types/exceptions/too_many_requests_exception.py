from dataclasses import dataclass, field
from http import HTTPStatus

from app.types.exceptions.bad_request_exception import BadRequestException


@dataclass(kw_only=True, slots=True)
class TooManyRequestsException(BadRequestException):
    error = BadRequestException.error + ".too_many_requests"

    detail: str = field(default="Too Many Requests")
    status_code: HTTPStatus = HTTPStatus.TOO_MANY_REQUESTS


__all__ = ("TooManyRequestsException",)
