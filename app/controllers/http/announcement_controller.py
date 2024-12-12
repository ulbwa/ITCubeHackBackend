from typing import Annotated

from annotated_types import Ge, Gt, Le
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from app import adapters, interfaces
from app.constraints import JSON_UTF8
from app.types import dto


class AnnouncementController(Controller):
    path = "/announcements"

    @get(media_type=JSON_UTF8)
    @inject
    async def search_announcements_handler(
        self,
        limit: Annotated[int, Gt(0), Le(30), Parameter(query="limit")] = 10,
        offset: Annotated[int, Ge(0), Parameter(query="offset")] = 0,
        *,
        announcement_repository: FromDishka[interfaces.AnnouncementRepository],
    ) -> list[dto.Announcement]:
        data = await announcement_repository.search(
            ensure_visible=True,
            limit=limit,
            offset=offset,
        )

        return [
            adapters.dto.AnnouncementDomainAdapter(announcement) for announcement in data
        ]


__all__ = ("AnnouncementController",)
