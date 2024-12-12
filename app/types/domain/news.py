from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.media import Media
from app.types.domain.news_gallery_item import NewsGalleryItem


@dataclass(kw_only=True, slots=True)
class News:
    ref_id: UUID
    title: str
    content: str
    is_hidden: bool
    created_at: datetime
    updated_at: datetime | None
    gallery: list[NewsGalleryItem]

    def get_media(self) -> Media:
        return self.gallery[0].media

    def get_publish_date(self) -> datetime:
        return self.updated_at or self.created_at


__all__ = ("NewsGalleryItem",)
