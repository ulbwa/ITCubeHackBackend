from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.media import Media

if TYPE_CHECKING:
    from app.database.schemas.study_program import StudyProgram


class StudyDirection(Base):
    __tablename__ = "study_directions"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    title: Mapped[str] = mapped_column(String(64))
    description: Mapped[str | None] = mapped_column(String(256))
    content: Mapped[str]
    media_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
    media_preview_media_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
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

    media: Mapped[Media] = relationship(foreign_keys=media_ref_id, lazy="selectin")
    media_preview: Mapped[Media] = relationship(
        foreign_keys=media_preview_media_ref_id, lazy="selectin"
    )
    programs: Mapped[list["StudyProgram"]] = relationship(
        back_populates="program", order_by="StudyProgram.created_at"
    )


__all__ = ("StudyDirection",)
