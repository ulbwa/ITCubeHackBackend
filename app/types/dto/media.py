from uuid import UUID

from pydantic import BaseModel, alias_generators

from app.types import enums


class Media(BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel):
    ref_id: UUID
    media_type: enums.MediaType
    photo_codec: enums.PhotoCodec | None
    file_uri: str


__all__ = ("Media",)
