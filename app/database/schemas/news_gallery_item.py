from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    SmallInteger,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.database.schemas.media import Media
from app.database.schemas.news import News


class NewsGalleryItem(Base):
    __tablename__ = "news_gallery"

    ref_id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    news_ref_id: Mapped[UUID] = mapped_column(ForeignKey(News.ref_id))
    media_ref_id: Mapped[UUID] = mapped_column(ForeignKey(Media.ref_id))
    index: Mapped[int] = mapped_column(SmallInteger)
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
    news: Mapped[News] = relationship(back_populates="gallery", foreign_keys=news_ref_id)

    __table_args__ = (
        CheckConstraint("index >= 0 AND index < 10"),
        UniqueConstraint("news_ref_id", "index"),
    )


__all__ = ("NewsGalleryItem",)
