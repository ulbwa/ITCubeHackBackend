from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.instructor import Instructor
from app.types.domain.media import Media
from app.types.domain.study_direction_review import StudyDirectionReview
from app.types.domain.study_program import StudyProgram


@dataclass(kw_only=True, slots=True)
class StudyDirection:
    ref_id: UUID
    title: str
    description: str | None
    content: str
    is_hidden: bool
    icon: Media
    created_at: datetime
    updated_at: datetime | None
    programs: list[StudyProgram]
    instructors: list[Instructor]
    reviews: list[StudyDirectionReview]


__all__ = ("Media",)
