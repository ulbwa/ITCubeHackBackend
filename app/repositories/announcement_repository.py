from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import adapters, interfaces
from app.database import schemas
from app.types import domain, enums


class AnnouncementRepository(interfaces.AnnouncementRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def search(
        self,
        ensure_visible: bool,
        sort_option: enums.AnnouncementSortOption,
        sort_direction: enums.SortDirection,
        limit: int,
        offset: int,
    ) -> interfaces.Sequence[domain.Announcement]:
        query = select(schemas.Announcement)

        if ensure_visible:
            query = query.where(schemas.Announcement.is_hidden.is_(False))

        if sort_option == enums.AnnouncementSortOption.CREATED_AT:
            if sort_direction == enums.SortDirection.ASC:
                query = query.order_by(schemas.Announcement.created_at.asc())
            else:
                query = query.order_by(schemas.Announcement.created_at.desc())

        if sort_option == enums.AnnouncementSortOption.DEFAULT:
            if sort_direction == enums.SortDirection.ASC:
                query = query.order_by(schemas.Announcement.index.asc())
            else:
                query = query.order_by(schemas.Announcement.index.desc())

        query = query.limit(limit).offset(offset)
        data = await self.session.scalars(query)

        return [
            adapters.domain.AnnouncementDatabaseAdapter(announcement)
            for announcement in data
        ]


__all__ = ("AnnouncementRepository",)
