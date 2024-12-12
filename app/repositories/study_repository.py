from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import noload

from app import adapters, interfaces
from app.database import schemas
from app.types import domain, exceptions


class StudyRepository(interfaces.StudyRepository):
    __slots__ = ("session",)

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, ref_id: UUID) -> domain.StudyDirection:
        query = select(schemas.StudyDirection).where(
            schemas.StudyDirection.ref_id == ref_id
        )
        data = await self.session.scalar(query)

        if not data:
            raise exceptions.NotFoundException()

        return adapters.domain.StudyDirectionDatabaseAdapter(data)

    async def get_program(self, ref_id: UUID) -> domain.StudyProgram:
        query = select(schemas.StudyProgram).where(schemas.StudyProgram.ref_id == ref_id)
        data = await self.session.scalar(query)

        if not data:
            raise exceptions.NotFoundException()

        return adapters.domain.StudyProgramDatabaseAdapter(data)

    async def search(
        self, ensure_visible: bool, limit: int, offset: int
    ) -> interfaces.Sequence[domain.StudyDirection]:
        query = select(schemas.StudyDirection).options(
            noload(schemas.StudyDirection.instructors)
        )

        if ensure_visible:
            query = query.where(schemas.StudyDirection.is_hidden.is_(False))

        query = (
            query.order_by(schemas.StudyDirection.created_at).limit(limit).offset(offset)
        )
        data = await self.session.scalars(query)

        return [
            adapters.domain.StudyDirectionDatabaseAdapter(direction)
            for direction in data
        ]


__all__ = ("StudyRepository",)
