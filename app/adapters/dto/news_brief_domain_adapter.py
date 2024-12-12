from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class NewsBriefDomainAdapter(dto.NewsBrief):
    def __init__(self, domain_obj: domain.News):
        super().__init__(
            ref_id=domain_obj.ref_id,
            title=domain_obj.title,
            publish_date=domain_obj.get_publish_date(),
            media=MediaDomainAdapter(domain_obj.get_media()),
        )


__all__ = ("NewsBriefDomainAdapter",)
