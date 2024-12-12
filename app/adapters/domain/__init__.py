from app.adapters.domain.announcement_database_adapter import (
    AnnouncementDatabaseAdapter,
)
from app.adapters.domain.instructor_database_adapter import InstructorDatabaseAdapter
from app.adapters.domain.media_database_adapter import MediaDatabaseAdapter
from app.adapters.domain.news_database_adapter import NewsDatabaseAdapter
from app.adapters.domain.news_gallery_item_database_adapter import (
    NewsGalleryItemDatabaseAdapter,
)
from app.adapters.domain.study_direction_database_adapter import (
    StudyDirectionDatabaseAdapter,
)
from app.adapters.domain.study_program_database_adapter import (
    StudyProgramDatabaseAdapter,
)

__all__ = (
    "AnnouncementDatabaseAdapter",
    "MediaDatabaseAdapter",
    "StudyDirectionDatabaseAdapter",
    "StudyProgramDatabaseAdapter",
    "InstructorDatabaseAdapter",
    "NewsDatabaseAdapter",
    "NewsGalleryItemDatabaseAdapter",
)
