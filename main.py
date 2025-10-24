from fastapi import HTTPException
from bootstraps.fast_api import BootstrapApp
from bootstraps.app.get_user_usecase import BootstrapGetUserUsecase
from app.get_user_usecase.get_user_usecase_input import GetUserUsecaseInput
from app.get_user_usecase.get_user_usecase_output import GetUserUsecaseOutputNotFound, User

app = BootstrapApp.get()
usecase = BootstrapGetUserUsecase.get()

@app.get("/")
async def root():
    return {"message": "¡Hola Mundo con FastAPI!"}

@app.get(
        "/users/{user_id}",
        response_model=User,
        tags=["users"],
        summary="Get a particular user by user_id",
        responses={
            404: {
                "description": "User not found",
            }
        }
)
async def get_user_by_user_id(user_id: int):
    usecase_input = GetUserUsecaseInput(user_id=user_id)
    usecase_output = usecase.execute(usecase_input)

    if isinstance(usecase_output, GetUserUsecaseOutputNotFound):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if isinstance(usecase_output, User):
        return usecase_output
