from typing import Annotated
from uuid import UUID

from annotated_types import Ge, Gt, Le
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from app import adapters, interfaces
from app.constraints import JSON_UTF8
from app.types import dto


class NewsController(Controller):
    path = "/news"

    @get("/{ref_id:uuid}", media_type=JSON_UTF8)
    @inject
    async def get_news_handler(
        self, ref_id: UUID, *, news_repository: FromDishka[interfaces.NewsRepository]
    ) -> dto.News:
        data = await news_repository.get(ref_id=ref_id)
        return adapters.dto.NewsDomainAdapter(data)

    @get(media_type=JSON_UTF8)
    @inject
    async def search_news_handler(
        self,
        limit: Annotated[int, Gt(0), Le(30), Parameter(query="limit")] = 10,
        offset: Annotated[int, Ge(0), Parameter(query="offset")] = 0,
        *,
        news_repository: FromDishka[interfaces.NewsRepository],
    ) -> list[dto.NewsBrief]:
        data = await news_repository.search(
            ensure_visible=True,
            limit=limit,
            offset=offset,
        )

        return [adapters.dto.NewsBriefDomainAdapter(direction) for direction in data]


__all__ = ("NewsController",)
