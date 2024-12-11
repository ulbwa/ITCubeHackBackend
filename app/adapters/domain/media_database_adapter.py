from app.database import schemas
from app.types import domain


class MediaDatabaseAdapter(domain.Media):
    def __init__(self, orm_obj: schemas.Media):
        super().__init__(
            ref_id=orm_obj.ref_id,
            bucket=orm_obj.bucket,
            file_key=orm_obj.file_key,
            media_type=orm_obj.media_type,
            photo_codec=orm_obj.photo_codec,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )


__all__ = ("MediaDatabaseAdapter",)
