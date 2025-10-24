from fastapi import HTTPException
from app.get_user_usecase.get_user_usecase import GetUserUsecase
from app.get_user_usecase.get_user_usecase_input import GetUserUsecaseInput
from app.get_user_usecase.get_user_usecase_output import GetUserUsecaseOutputNotFound, User

class GetUserByUserIdController:
    _usecase: GetUserUsecase

    def __init__(
            self,
            usecase: GetUserUsecase
    ):
      self._usecase = usecase

    def execute(self, user_id: int):
        usecase_input = GetUserUsecaseInput(user_id=user_id)
        usecase_output = self._usecase.execute(input=usecase_input)

        if isinstance(usecase_output, GetUserUsecaseOutputNotFound):
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
    
        if isinstance(usecase_output, User):
            return usecase_output