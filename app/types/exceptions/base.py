from dataclasses import dataclass, fields
from http import HTTPStatus
from typing import ClassVar


@dataclass(kw_only=True, slots=True)
class APIException(Exception):
    error: ClassVar[str]
    status_code: HTTPStatus
    detail: str
    headers: dict[str, str] | None = None

    def __str__(self) -> str:
        detail = []
        for field in fields(self):
            if not field.repr:
                continue
            detail.append(f"{field.name}={getattr(self, field.name)!r}")
        return ", ".join(detail)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self)})"


__all__ = ("APIException",)
