from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.instructor import Instructor
from app.database.schemas.media import Media

if TYPE_CHECKING:
    from app.database.schemas.study_direction_review import StudyDirectionReview
    from app.database.schemas.study_program import StudyProgram


class StudyDirection(Base):
    __tablename__ = "study_directions"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str | None] = mapped_column(String(512))
    content: Mapped[str]
    is_hidden: Mapped[bool]
    icon_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
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

    icon: Mapped[Media] = relationship(foreign_keys=icon_ref_id, lazy="selectin")
    programs: Mapped[list["StudyProgram"]] = relationship(
        back_populates="direction", order_by="StudyProgram.created_at", lazy="selectin"
    )
    instructors: Mapped[list[Instructor]] = relationship(
        secondary="study_direction_instructor_relatinoship", lazy="selectin"
    )
    reviews: Mapped[list["StudyDirectionReview"]] = relationship(lazy="selectin")


__all__ = ("StudyDirection",)
