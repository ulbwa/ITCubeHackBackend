from abc import abstractmethod
from typing import Protocol, Sequence
from uuid import UUID

from app.types import domain


class AnnouncementRepository(Protocol):
    @abstractmethod
    async def search(
        self,
        ensure_visible: bool,
        limit: int,
        offset: int,
    ) -> Sequence[domain.Announcement]: ...


class StudyRepository(Protocol):
    @abstractmethod
    async def get(self, ref_id: UUID) -> domain.StudyDirection: ...

    @abstractmethod
    async def get_program(self, ref_id: UUID) -> domain.StudyProgram: ...

    @abstractmethod
    async def search(
        self, ensure_visible: bool, limit: int, offset: int
    ) -> Sequence[domain.StudyDirection]: ...


class MediaRepository(Protocol):
    @abstractmethod
    async def get(self, ref_id: UUID) -> domain.Media: ...


class NewsRepository(Protocol):
    @abstractmethod
    async def get(self, ref_id: UUID) -> domain.News: ...

    @abstractmethod
    async def search(
        self, ensure_visible: bool, limit: int, offset: int
    ) -> Sequence[domain.News]: ...


__all__ = "AnnouncementRepository", "StudyRepository", "MediaRepository"
