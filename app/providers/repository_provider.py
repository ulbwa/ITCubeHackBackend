from dishka import Provider, Scope, provide

from app import interfaces, repositories


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    announcement_repository = provide(
        repositories.AnnouncementRepository,
        provides=interfaces.AnnouncementRepository,
    )


__all__ = ("RepositoryProvider",)
