from app.adapters.domain.news_gallery_item_database_adapter import (
    NewsGalleryItemDatabaseAdapter,
)
from app.database import schemas
from app.types import domain


class NewsDatabaseAdapter(domain.News):
    def __init__(self, orm_obj: schemas.News):
        super().__init__(
            ref_id=orm_obj.ref_id,
            title=orm_obj.title,
            content=orm_obj.content,
            is_hidden=orm_obj.is_hidden,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
            gallery=[
                NewsGalleryItemDatabaseAdapter(gallery_item)
                for gallery_item in orm_obj.gallery
            ],
        )


__all__ = ("NewsDatabaseAdapter",)
