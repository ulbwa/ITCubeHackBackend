from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.database import schemas
from app.types import domain


class InstructorDatabaseAdapter(domain.Instructor):
    def __init__(self, orm_obj: schemas.Instructor):
        super().__init__(
            ref_id=orm_obj.ref_id,
            first_name=orm_obj.first_name,
            last_name=orm_obj.last_name,
            middle_name=orm_obj.middle_name,
            description=orm_obj.description,
            seniority=orm_obj.seniority,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            media=MediaDatabaseAdapter(orm_obj.media),
        )


__all__ = ("InstructorDatabaseAdapter",)
