from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types.dto.media import Media
from app.types.dto.study_program import StudyProgram


class StudyDirection(
    BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel
):
    ref_id: UUID
    title: str
    content: str
    media: Media
    programs: Sequence[StudyProgram]


__all__ = ("StudyDirection",)
