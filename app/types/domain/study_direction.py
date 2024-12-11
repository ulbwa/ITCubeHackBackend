from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.media import Media
from app.types.domain.study_program import StudyProgram


@dataclass(kw_only=True, slots=True)
class StudyDirection:
    ref_id: UUID
    title: str
    description: str
    content: str
    media: Media
    media_preview: Media
    created_at: datetime
    updated_at: datetime | None
    programs: list[StudyProgram]


__all__ = ("Media",)
