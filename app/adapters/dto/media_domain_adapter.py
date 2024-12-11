from app.types import domain, dto


class MediaDomainAdapter(dto.Media):
    def __init__(self, domain_obj: domain.Media):
        super().__init__(
            ref_id=domain_obj.ref_id,
            media_type=domain_obj.media_type,
            photo_codec=domain_obj.photo_codec,
            file_uri=domain_obj.get_file_uri(),
        )


__all__ = ("MediaDomainAdapter",)
