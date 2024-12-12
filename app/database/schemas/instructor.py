from datetime import datetime, timedelta
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.media import Media


class Instructor(Base):
    __tablename__ = "instructors"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    middle_name: Mapped[str | None] = mapped_column(String(32))
    description: Mapped[str | None] = mapped_column(String(512))
    seniority: Mapped[timedelta]
    media_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
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


__all__ = ("Media",)
