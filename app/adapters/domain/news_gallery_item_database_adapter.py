from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.database import schemas
from app.types import domain


class NewsGalleryItemDatabaseAdapter(domain.NewsGalleryItem):
    def __init__(self, orm_obj: schemas.NewsGalleryItem):
        super().__init__(
            ref_id=orm_obj.ref_id,
            news_ref_id=orm_obj.news_ref_id,
            index=orm_obj.index,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            media=MediaDatabaseAdapter(orm_obj.media),
        )


__all__ = ("NewsGalleryItemDatabaseAdapter",)
