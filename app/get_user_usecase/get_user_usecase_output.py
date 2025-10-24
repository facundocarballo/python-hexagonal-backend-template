from dataclasses import dataclass
from domain.entities.user import User

@dataclass
class GetUserUsecaseOutputNotFound:
    user_id: int


@dataclass
class GetUserUsecaseInput:
    user_id: int

type GetUserUsecaseOutput = User | GetUserUsecaseOutputNotFound