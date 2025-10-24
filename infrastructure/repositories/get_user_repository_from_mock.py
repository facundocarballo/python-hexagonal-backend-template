from domain.entities.user import User
from domain.ports.repositories.get_user_repository.get_user_repository import GetUserRepository
from domain.ports.repositories.get_user_repository.get_user_repository_input import GetUserRepositoryInput

class GetUserRepositoryFromMock(GetUserRepository):    
    def execute(self, input: GetUserRepositoryInput) -> User | None:
        mock_user_list = {
            1: User(
                id=1, 
                username="facundocarballo", 
                email="carballofacundo70@gmail.com", 
                first_name="Facundo", 
                last_name="Carballo"
            ),
            2: User(
                id=2, 
                username="fast-api", 
                email="fast-api@gmail.com", 
                first_name="Fast", 
                last_name="Api"
            )
        }
        
        return mock_user_list.get(input.user_id)
