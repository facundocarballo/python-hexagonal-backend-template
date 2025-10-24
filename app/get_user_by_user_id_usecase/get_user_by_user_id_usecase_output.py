from dataclasses import dataclass
from domain.entities.user import User

@dataclass
class GetUserByUserIdUsecaseOutputNotFound:
    user_id: int

type GetUserByUserIdUsecaseOutput = User | GetUserByUserIdUsecaseOutputNotFound