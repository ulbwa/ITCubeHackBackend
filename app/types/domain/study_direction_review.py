from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.study_program import StudyProgram


@dataclass(kw_only=True, slots=True)
class StudyDirectionReview:
    ref_id: UUID
    direction_ref_id: UUID
    author: str
    title: str
    description: str
    rating: int
    created_at: datetime
    updated_at: datetime | None
    program: StudyProgram


__all__ = ("StudyDirectionReview",)
