from app.get_user_usecase.get_user_usecase import GetUserUsecase
from bootstraps.infrastructure.repositories.get_user_repository_mock import BootstrapGetUserRepositoryMock

class BootstrapGetUserUsecase:
    _instance: GetUserUsecase | None = None

    @classmethod
    def get(cls) -> GetUserUsecase:
        if cls._instance is None:
            get_user_repository = BootstrapGetUserRepositoryMock.get()
            cls._instance = GetUserUsecase(get_user_repository)
        return cls._instance