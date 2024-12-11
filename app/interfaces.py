from abc import abstractmethod
from typing import Protocol, Sequence

from app.types import domain, enums


class AnnouncementRepository(Protocol):
    @abstractmethod
    async def search(
        self,
        ensure_visible: bool,
        sort_option: enums.AnnouncementSortOption,
        sort_direction: enums.SortDirection,
        limit: int,
        offset: int,
    ) -> Sequence[domain.Announcement]: ...


__all__ = ("AnnouncementRepository",)
