from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

from app.database import schemas  # noqa: E402

__all__ = "metadata", "Base", "schemas"
