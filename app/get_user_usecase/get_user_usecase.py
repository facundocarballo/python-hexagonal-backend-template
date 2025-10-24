from dataclasses import dataclass
from domain.ports.repositories.get_user_repository.get_user_repository import GetUserRepository
from domain.ports.repositories.get_user_repository.get_user_repository_input import GetUserRepositoryInput
from app.get_user_usecase.get_user_usecase_input import GetUserUsecaseInput
from app.get_user_usecase.get_user_usecase_output import GetUserUsecaseOutput, GetUserUsecaseOutputNotFound

class GetUserUsecase:
    _get_user_repository: GetUserRepository

    def __init__(
            self, 
            get_user_repository: GetUserRepository
    ):
        self._get_user_repository = get_user_repository

    def execute(self, input: GetUserUsecaseInput) -> GetUserUsecaseOutput:
        repository_input = GetUserRepositoryInput(input.user_id)
        user = self._get_user_repository.execute(repository_input)
        
        if user is None:
            return GetUserUsecaseOutputNotFound(input.user_id)
        
        return user