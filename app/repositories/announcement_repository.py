from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import adapters, interfaces
from app.database import schemas
from app.types import domain


class AnnouncementRepository(interfaces.AnnouncementRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def search(
        self,
        ensure_visible: bool,
        limit: int,
        offset: int,
    ) -> interfaces.Sequence[domain.Announcement]:
        query = select(schemas.Announcement).order_by(schemas.Announcement.index)

        if ensure_visible:
            query = query.where(schemas.Announcement.is_hidden.is_(False))

        query = query.limit(limit).offset(offset)
        data = await self.session.scalars(query)

        return [
            adapters.domain.AnnouncementDatabaseAdapter(announcement)
            for announcement in data
        ]


__all__ = ("AnnouncementRepository",)
