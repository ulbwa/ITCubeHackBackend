from app.adapters.dto.instructor_domain_adapter import InstructorDomainAdapter
from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.adapters.dto.study_direction_review_domain_adapter import (
    StudyDirectionReviewDomainAdapter,
)
from app.adapters.dto.study_program_domain_adapter import StudyProgramDomainAdapter
from app.types import domain, dto


class StudyDirectionDomainAdapter(dto.StudyDirection):
    def __init__(self, domain_obj: domain.StudyDirection):
        super().__init__(
            ref_id=domain_obj.ref_id,
            title=domain_obj.title,
            content=domain_obj.content,
            icon=MediaDomainAdapter(domain_obj.icon),
            programs=[
                StudyProgramDomainAdapter(program) for program in domain_obj.programs
            ],
            instructors=[
                InstructorDomainAdapter(instructor)
                for instructor in domain_obj.instructors
            ],
            reviews=[
                StudyDirectionReviewDomainAdapter(review)
                for review in domain_obj.reviews
            ],
        )


__all__ = ("StudyDirectionDomainAdapter",)
