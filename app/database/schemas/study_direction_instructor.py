from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class StudyDirectionInstructor(Base):
    __tablename__ = "study_direction_instructor_relatinoship"

    study_direction_ref_id: Mapped[UUID] = mapped_column(
        ForeignKey("study_directions.ref_id"), primary_key=True
    )
    instructor_ref_id: Mapped[UUID] = mapped_column(
        ForeignKey("instructors.ref_id"), primary_key=True
    )

    __table_args__ = (UniqueConstraint(study_direction_ref_id, instructor_ref_id),)


__all__ = ("StudyDirectionInstructor",)
