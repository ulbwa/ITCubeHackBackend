from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import adapters, interfaces
from app.database import schemas
from app.types import domain, exceptions


class NewsRepository(interfaces.NewsRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, ref_id: UUID) -> domain.News:
        query = select(schemas.News).where(schemas.News.ref_id == ref_id)
        data = await self.session.scalar(query)
        if not data:
            raise exceptions.NotFoundException()
        return adapters.domain.NewsDatabaseAdapter(data)

    async def search(
        self, ensure_visible: bool, limit: int, offset: int
    ) -> interfaces.Sequence[domain.News]:
        query = select(schemas.News).order_by(schemas.News.created_at)

        if ensure_visible:
            query = query.where(schemas.News.is_hidden.is_(False))

        query = query.limit(limit).offset(offset)
        data = await self.session.scalars(query)

        return [adapters.domain.NewsDatabaseAdapter(news) for news in data]


__all__ = ("NewsRepository",)
