from typing import Annotated
from uuid import UUID

from annotated_types import Ge, Gt, Le
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from app import adapters, interfaces
from app.constraints import JSON_UTF8
from app.types import dto


class StudyController(Controller):
    path = "/study"

    @get("/{ref_id:uuid}", media_type=JSON_UTF8)
    @inject
    async def get_study_direction_handler(
        self, ref_id: UUID, *, study_repository: FromDishka[interfaces.StudyRepository]
    ) -> dto.StudyDirection:
        data = await study_repository.get(ref_id=ref_id)
        return adapters.dto.StudyDirectionDomainAdapter(data)

    @get("/program/{ref_id:uuid}", media_type=JSON_UTF8)
    @inject
    async def get_study_program_handler(
        self, ref_id: UUID, *, study_repository: FromDishka[interfaces.StudyRepository]
    ) -> dto.StudyProgram:
        data = await study_repository.get_program(ref_id=ref_id)
        return adapters.dto.StudyProgramDomainAdapter(data)

    @get(media_type=JSON_UTF8)
    @inject
    async def search_study_directions_handler(
        self,
        limit: Annotated[int, Gt(0), Le(30), Parameter(query="limit")] = 10,
        offset: Annotated[int, Ge(0), Parameter(query="offset")] = 0,
        *,
        study_repository: FromDishka[interfaces.StudyRepository],
    ) -> list[dto.StudyDirectionBrief]:
        data = await study_repository.search(
            ensure_visible=True,
            limit=limit,
            offset=offset,
        )

        return [
            adapters.dto.StudyDirectionBriefDomainAdapter(direction)
            for direction in data
        ]


__all__ = ("StudyController",)
