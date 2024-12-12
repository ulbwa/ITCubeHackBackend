from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class NewsDomainAdapter(dto.News):
    def __init__(self, domain_obj: domain.News):
        super().__init__(
            ref_id=domain_obj.ref_id,
            title=domain_obj.title,
            content=domain_obj.content,
            publish_date=domain_obj.get_publish_date(),
            gallery=[
                MediaDomainAdapter(gallery_item.media)
                for gallery_item in domain_obj.gallery
            ],
        )


__all__ = ("NewsDomainAdapter",)
