from app.adapters.dto.announcement_domain_adapter import AnnouncementDomainAdapter
from app.adapters.dto.instructor_domain_adapter import InstructorDomainAdapter
from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.adapters.dto.news_brief_domain_adapter import NewsBriefDomainAdapter
from app.adapters.dto.news_domain_adapter import NewsDomainAdapter
from app.adapters.dto.study_direction_brief_domain_adapter import (
    StudyDirectionBriefDomainAdapter,
)
from app.adapters.dto.study_direction_domain_adapter import StudyDirectionDomainAdapter
from app.adapters.dto.study_program_domain_adapter import StudyProgramDomainAdapter

__all__ = (
    "AnnouncementDomainAdapter",
    "MediaDomainAdapter",
    "StudyDirectionBriefDomainAdapter",
    "StudyDirectionDomainAdapter",
    "StudyProgramDomainAdapter",
    "NewsDomainAdapter",
    "InstructorDomainAdapter",
    "NewsBriefDomainAdapter",
)
