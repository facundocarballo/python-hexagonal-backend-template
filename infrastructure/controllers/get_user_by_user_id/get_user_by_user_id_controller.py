from fastapi import HTTPException
from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase import GetUserByUserIdUsecase
from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase_input import GetUserByUserIdUsecaseInput
from app.get_user_by_user_id_usecase.get_user_by_user_id_usecase_output import GetUserByUserIdUsecaseOutputNotFound, User

class GetUserByUserIdController:
    _usecase: GetUserByUserIdUsecase

    def __init__(
            self,
            usecase: GetUserByUserIdUsecase
    ):
      self._usecase = usecase

    def execute(self, user_id: int):
        usecase_input = GetUserByUserIdUsecaseInput(user_id=user_id)
        usecase_output = self._usecase.execute(input=usecase_input)

        if isinstance(usecase_output, GetUserByUserIdUsecaseOutputNotFound):
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
    
        if isinstance(usecase_output, User):
            return usecase_output