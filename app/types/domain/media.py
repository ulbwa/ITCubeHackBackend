from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.types import enums


@dataclass(kw_only=True, slots=True)
class Media:
    ref_id: UUID
    bucket: str
    file_key: str
    media_type: enums.MediaType
    photo_codec: enums.PhotoCodec | None
    created_at: datetime
    updated_at: datetime | None

    def get_file_uri(self) -> str:
        return f"/storage/{self.ref_id}"

    def get_file_key(self) -> str:
        return f"{self.bucket}/{self.file_key}"


__all__ = ("Media",)
