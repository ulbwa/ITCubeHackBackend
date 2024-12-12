from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import adapters, interfaces
from app.database import schemas
from app.types import domain, exceptions


class MediaRepository(interfaces.MediaRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, ref_id: UUID) -> domain.Media:
        query = select(schemas.Media).where(schemas.Media.ref_id == ref_id)
        data = await self.session.scalar(query)
        if not data:
            raise exceptions.NotFoundException()
        return adapters.domain.MediaDatabaseAdapter(data)


__all__ = ("MediaRepository",)
