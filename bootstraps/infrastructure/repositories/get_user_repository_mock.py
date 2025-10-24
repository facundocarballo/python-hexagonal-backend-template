from domain.ports.repositories.get_user_repository.get_user_repository import GetUserRepository
from infrastructure.repositories.get_user_repository_from_mock import GetUserRepositoryFromMock

class BootstrapGetUserRepositoryMock:
    _instance: GetUserRepository | None = None

    @classmethod
    def get(cls) -> GetUserRepository:
        if cls._instance is None:
            cls._instance = GetUserRepositoryFromMock()
        return cls._instance