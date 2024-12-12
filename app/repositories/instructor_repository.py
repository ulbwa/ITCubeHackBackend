from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import adapters, interfaces
from app.database import schemas
from app.types import domain


class InstructorRepository(interfaces.InstructorRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def search(
        self,
        limit: int,
        offset: int,
    ) -> Sequence[domain.Instructor]:
        query = select(schemas.Instructor).order_by(schemas.Instructor.created_at)

        query = query.limit(limit).offset(offset)
        data = await self.session.scalars(query)

        return [
            adapters.domain.InstructorDatabaseAdapter(announcement)
            for announcement in data
        ]


__all__ = ("InstructorRepository",)
