from infrastructure.controllers.get_user_by_user_id.get_user_by_user_id_controller import GetUserByUserIdController
from bootstraps.app.get_user_by_user_id_usecase import BootstrapGetUserByUserIdUsecase

class BootstrapGetUserByUserIdController:
    _instance: GetUserByUserIdController | None = None

    @classmethod
    def get(cls) -> GetUserByUserIdController:
        if cls._instance is None:
            usecase = BootstrapGetUserByUserIdUsecase.get()
            cls._instance = GetUserByUserIdController(usecase)
        return cls._instance