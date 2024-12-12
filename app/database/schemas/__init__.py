from app.database.schemas.announcement import Announcement
from app.database.schemas.instructor import Instructor
from app.database.schemas.media import Media
from app.database.schemas.news import News
from app.database.schemas.news_gallery_item import NewsGalleryItem
from app.database.schemas.study_direction import StudyDirection
from app.database.schemas.study_direction_instructor import StudyDirectionInstructor
from app.database.schemas.study_program import StudyProgram

__all__ = (
    "Announcement",
    "Media",
    "News",
    "NewsGalleryItem",
    "StudyDirection",
    "StudyProgram",
    "Instructor",
    "StudyDirectionInstructor",
)
