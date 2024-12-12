from app.adapters.dto.media_domain_adapter import MediaDomainAdapter
from app.types import domain, dto


class StudyProgramDomainAdapter(dto.StudyProgram):
    def __init__(self, domain_obj: domain.StudyProgram):
        super().__init__(
            ref_id=domain_obj.ref_id,
            title=domain_obj.title,
            description=domain_obj.description,
            document=MediaDomainAdapter(domain_obj.document),
        )


__all__ = ("MediaDomainAdapter",)
