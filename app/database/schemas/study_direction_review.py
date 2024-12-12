from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    SmallInteger,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.study_program import StudyProgram


class StudyDirectionReview(Base):
    __tablename__ = "study_direction_reviews"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    direction_ref_id: Mapped[UUID] = mapped_column(ForeignKey("study_directions.ref_id"))
    program_ref_id: Mapped[UUID] = mapped_column(ForeignKey(StudyProgram.ref_id))
    author: Mapped[str] = mapped_column(String(128))
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(512))
    rating: Mapped[int] = mapped_column(SmallInteger())
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

    program: Mapped[StudyProgram] = relationship(
        lazy="selectin", foreign_keys=program_ref_id
    )

    __table_args__ = (CheckConstraint("rating >= 0 AND rating <= 5"),)


__all__ = ("StudyProgram",)
