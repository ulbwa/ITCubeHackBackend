from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types.dto.media import Media


class Announcement(
    BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel
):
    ref_id: UUID
    url: str
    media: Media


__all__ = ("Announcement",)
