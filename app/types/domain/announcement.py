from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.media import Media


@dataclass(kw_only=True, slots=True)
class Announcement:
    ref_id: UUID
    index: int
    is_hidden: bool
    url: str
    created_at: datetime
    updated_at: datetime | None
    media: Media


__all__ = ("Announcement",)
