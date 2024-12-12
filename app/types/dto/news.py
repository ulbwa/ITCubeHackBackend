from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types.dto.media import Media


class News(BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel):
    ref_id: UUID
    title: str
    content: str
    publish_date: datetime
    gallery: list[Media]


__all__ = ("News",)
