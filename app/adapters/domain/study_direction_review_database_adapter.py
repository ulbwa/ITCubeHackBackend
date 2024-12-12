from app.adapters.domain.study_program_database_adapter import (
    StudyProgramDatabaseAdapter,
)
from app.database import schemas
from app.types import domain


class StudyDirectionReviewDatabaseAdapter(domain.StudyDirectionReview):
    def __init__(self, orm_obj: schemas.StudyDirectionReview):
        super().__init__(
            ref_id=orm_obj.ref_id,
            direction_ref_id=orm_obj.direction_ref_id,
            author=orm_obj.author,
            title=orm_obj.title,
            description=orm_obj.description,
            rating=orm_obj.rating,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            program=StudyProgramDatabaseAdapter(orm_obj.program),
        )


__all__ = ("StudyDirectionReviewDatabaseAdapter",)
