from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    SmallInteger,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.media import Media


class Announcement(Base):
    __tablename__ = "announcements"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    index: Mapped[int] = mapped_column(SmallInteger, unique=True)
    is_hidden: Mapped[bool]
    media_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
    url: Mapped[str] = mapped_column(String(128))
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

    media: Mapped[Media] = relationship(foreign_keys=media_ref_id, lazy="selectin")

    __table_args__ = (CheckConstraint("index >= 0"),)


__all__ = ("Announcement",)
