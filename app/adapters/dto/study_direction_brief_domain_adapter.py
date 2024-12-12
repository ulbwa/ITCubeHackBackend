from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class StudyDirectionBriefDomainAdapter(dto.StudyDirectionBrief):
    def __init__(self, domain_obj: domain.StudyDirection):
        super().__init__(
            ref_id=domain_obj.ref_id,
            title=domain_obj.title,
            description=domain_obj.description,
            icon=MediaDomainAdapter(domain_obj.icon),
        )


__all__ = ("StudyDirectionBriefDomainAdapter",)
