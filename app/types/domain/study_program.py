from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types.domain.media import Media


@dataclass(kw_only=True, slots=True)
class StudyProgram:
    ref_id: UUID
    program_ref_id: UUID
    title: str
    description: str | None
    document: Media
    created_at: datetime
    updated_at: datetime | None


__all__ = ("Media",)
