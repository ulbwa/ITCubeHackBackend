from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types.dto.media import Media


class Instructor(
    BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel
):
    ref_id: UUID
    display_name: str
    display_short_name: str
    description: str | None
    display_seniority: str
    media: Media


__all__ = ("Instructor",)
