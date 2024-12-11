from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.types import enums


class Media(Base):
    __tablename__ = "media"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    bucket: Mapped[str] = mapped_column(String(32))
    file_key: Mapped[str] = mapped_column(String(64))
    media_type: Mapped[enums.MediaType]
    photo_codec: Mapped[enums.PhotoCodec | None]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now,
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
        server_default=text("NULL"),
        onupdate=datetime.now,
        server_onupdate=func.now(),
        index=True,
    )

    __table_args__ = (
        CheckConstraint(
            "(media_type != 'PHOTO' AND photo_codec IS NULL) OR (media_type = 'PHOTO' AND photo_codec IS NOT NULL)"  # noqa: E501
        ),
    )


__all__ = ("Media",)
