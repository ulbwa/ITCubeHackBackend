from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class AnnouncementDomainAdapter(dto.Announcement):
    def __init__(self, domain_obj: domain.Announcement):
        super().__init__(
            ref_id=domain_obj.ref_id,
            url=domain_obj.url,
            media=MediaDomainAdapter(domain_obj.media),
        )


__all__ = ("AnnouncementDomainAdapter",)
