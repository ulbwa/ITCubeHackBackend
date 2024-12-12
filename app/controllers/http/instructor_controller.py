from typing import Annotated

from annotated_types import Ge, Gt, Le
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from app import adapters, interfaces
from app.constraints import JSON_UTF8
from app.types import dto


class InstructorController(Controller):
    path = "/instructors"

    @get(media_type=JSON_UTF8)
    @inject
    async def search_instructors_handler(
        self,
        limit: Annotated[int, Gt(0), Le(30), Parameter(query="limit")] = 10,
        offset: Annotated[int, Ge(0), Parameter(query="offset")] = 0,
        *,
        instructor_repository: FromDishka[interfaces.InstructorRepository],
    ) -> list[dto.Instructor]:
        data = await instructor_repository.search(
            limit=limit,
            offset=offset,
        )

        return [adapters.dto.InstructorDomainAdapter(direction) for direction in data]


__all__ = ("InstructorController",)
