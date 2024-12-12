from dishka import Provider, Scope, provide

from app import interfaces, repositories


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    announcement_repository = provide(
        repositories.AnnouncementRepository,
        provides=interfaces.AnnouncementRepository,
    )
    study_repository = provide(
        repositories.StudyRepository,
        provides=interfaces.StudyRepository,
    )
    media_repository = provide(
        repositories.MediaRepository,
        provides=interfaces.MediaRepository,
    )


__all__ = ("RepositoryProvider",)
