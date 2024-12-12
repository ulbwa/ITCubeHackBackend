from app.types import domain, dto


class StudyDirectionReviewDomainAdapter(dto.StudyDirectionReview):
    def __init__(self, domain_obj: domain.StudyDirectionReview):
        super().__init__(
            ref_id=domain_obj.ref_id,
            author=domain_obj.author,
            title=domain_obj.title,
            description=domain_obj.description,
            rating=domain_obj.rating,
            program_title=domain_obj.program.title,
        )


__all__ = ("StudyDirectionReviewDomainAdapter",)
