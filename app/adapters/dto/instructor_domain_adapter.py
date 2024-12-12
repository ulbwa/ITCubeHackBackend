from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class InstructorDomainAdapter(dto.Instructor):
    def __init__(self, domain_obj: domain.Instructor):
        super().__init__(
            ref_id=domain_obj.ref_id,
            display_name=domain_obj.get_display_name(),
            display_short_name=domain_obj.get_display_short_name(),
            description=domain_obj.description,
            display_seniority=domain_obj.get_display_seniority(),
            media=MediaDomainAdapter(domain_obj.media),
        )


__all__ = ("InstructorDomainAdapter",)
