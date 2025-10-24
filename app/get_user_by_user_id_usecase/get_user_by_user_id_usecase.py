from dataclasses import dataclass
from domain.ports.repositories.get_user_repository.get_user_repository import GetUserRepository
from domain.ports.repositories.get_user_repository.get_user_repository_input import GetUserRepositoryInput
from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase_input import GetUserByUserIdUsecaseInput
from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase_output import GetUserByUserIdUsecaseOutput, GetUserByUserIdUsecaseOutputNotFound

class GetUserByUserIdUsecase:
    _get_user_repository: GetUserRepository

    def __init__(
            self, 
            get_user_repository: GetUserRepository
    ):
        self._get_user_repository = get_user_repository

    def execute(self, input: GetUserByUserIdUsecaseInput) -> GetUserByUserIdUsecaseOutput:
        repository_input = GetUserRepositoryInput(input.user_id)
        user = self._get_user_repository.execute(repository_input)
        
        if user is None:
            return GetUserByUserIdUsecaseOutputNotFound(input.user_id)
        
        return user