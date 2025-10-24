from abc import ABC, abstractmethod
from domain.ports.repositories.get_user_repository.get_user_repository_input import GetUserRepositoryInput
from domain.entities.user import User

class GetUserRepository(ABC):
    @abstractmethod
    def execute(self, input: GetUserRepositoryInput) -> User | None:
        pass