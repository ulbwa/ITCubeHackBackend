from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.media import Media


@dataclass(kw_only=True, slots=True)
class NewsGalleryItem:
    ref_id: UUID
    news_ref_id: UUID
    index: int
    created_at: datetime
    updated_at: datetime | None
    media: Media


__all__ = ("NewsGalleryItem",)
