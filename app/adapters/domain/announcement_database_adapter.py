from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.database import schemas
from app.types import domain


class AnnouncementDatabaseAdapter(domain.Announcement):
    def __init__(self, orm_obj: schemas.Announcement):
        super().__init__(
            ref_id=orm_obj.ref_id,
            index=orm_obj.index,
            is_hidden=orm_obj.is_hidden,
            url=orm_obj.url,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            media=MediaDatabaseAdapter(orm_obj.media),
        )


__all__ = ("MediaDatabaseAdapter",)
