from typing import Annotated

from annotated_types import Ge, Gt, Le
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from app import adapters, interfaces
from app.constraints import JSON_UTF8
from app.types import dto, enums


class AnnouncementController(Controller):
    path = "/announcements"

    @get(media_type=JSON_UTF8)
    @inject
    async def search_announcements_handler(
        self,
        sort_option: Annotated[
            enums.AnnouncementSortOption, Parameter(query="sortOption")
        ] = enums.AnnouncementSortOption.DEFAULT,
        sort_direction: Annotated[
            enums.SortDirection, Parameter(query="sortDirection")
        ] = enums.SortDirection.ASC,
        limit: Annotated[int, Gt(0), Le(30), Parameter(query="limit")] = 10,
        offset: Annotated[int, Ge(0), Parameter(query="offset")] = 0,
        *,
        announcement_repository: FromDishka[interfaces.AnnouncementRepository],
    ) -> list[dto.Announcement]:
        data = await announcement_repository.search(
            ensure_visible=True,
            sort_option=sort_option,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )

        return [
            adapters.dto.AnnouncementDomainAdapter(announcement) for announcement in data
        ]


__all__ = ("AnnouncementController",)
