from app.adapters.domain.instructor_database_adapter import InstructorDatabaseAdapter
from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.adapters.domain.study_program_database_adapter import (
    StudyProgramDatabaseAdapter,
)
from app.database import schemas
from app.types import domain


class StudyDirectionDatabaseAdapter(domain.StudyDirection):
    def __init__(self, orm_obj: schemas.StudyDirection):
        super().__init__(
            ref_id=orm_obj.ref_id,
            title=orm_obj.title,
            description=orm_obj.description,
            content=orm_obj.content,
            is_hidden=orm_obj.is_hidden,
            icon=MediaDatabaseAdapter(orm_obj.icon),
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            programs=[
                StudyProgramDatabaseAdapter(program) for program in orm_obj.programs
            ],
            instructors=[
                InstructorDatabaseAdapter(instructor)
                for instructor in orm_obj.instructors
            ],
        )


__all__ = ("MediaDatabaseAdapter",)
