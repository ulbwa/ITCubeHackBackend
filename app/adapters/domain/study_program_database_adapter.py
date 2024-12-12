from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.database import schemas
from app.types import domain


class StudyProgramDatabaseAdapter(domain.StudyProgram):
    def __init__(self, orm_obj: schemas.StudyProgram):
        super().__init__(
            ref_id=orm_obj.ref_id,
            direction_ref_id=orm_obj.direction_ref_id,
            title=orm_obj.title,
            description=orm_obj.description,
            document=MediaDatabaseAdapter(orm_obj.document),
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )


__all__ = ("MediaDatabaseAdapter",)
