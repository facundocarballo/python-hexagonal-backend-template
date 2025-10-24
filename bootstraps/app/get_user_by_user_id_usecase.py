from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase import GetUserByUserIdUsecase
from bootstraps.infrastructure.repositories.get_user_repository_mock import BootstrapGetUserRepositoryMock

class BootstrapGetUserByUserIdUsecase:
    _instance: GetUserByUserIdUsecase | None = None

    @classmethod
    def get(cls) -> GetUserByUserIdUsecase:
        if cls._instance is None:
            get_user_repository = BootstrapGetUserRepositoryMock.get()
            cls._instance = GetUserByUserIdUsecase(get_user_repository)
        return cls._instance