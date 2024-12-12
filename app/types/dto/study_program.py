from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types.dto.media import Media


class StudyProgram(
    BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel
):
    ref_id: UUID
    title: str
    description: str | None
    document: Media


__all__ = ("StudyProgram",)
