from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.media import Media
from app.database.schemas.study_direction import StudyDirection


class StudyProgram(Base):
    __tablename__ = "study_programs"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    direction_ref_id: Mapped[UUID] = mapped_column(ForeignKey(StudyDirection.ref_id))
    title: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(256))
    document_ref_id: Mapped[Media] = mapped_column(ForeignKey(Media.ref_id))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now,
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
        server_default=text("NULL"),
        onupdate=datetime.now,
        server_onupdate=func.now(),
        index=True,
    )

    document: Mapped[Media] = relationship(foreign_keys=document_ref_id, lazy="selectin")
    direction: Mapped[StudyDirection] = relationship(foreign_keys=direction_ref_id)


__all__ = ("StudyProgram",)
