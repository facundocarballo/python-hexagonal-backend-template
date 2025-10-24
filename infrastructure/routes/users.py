from fastapi import APIRouter
from domain.entities.user import User
from bootstraps.infrastructure.controllers.get_user_by_user_id_controller import BootstrapGetUserByUserIdController

# Router
UsersRouter = APIRouter()

# Controllers
get_user_by_user_id_controller = BootstrapGetUserByUserIdController.get()

@UsersRouter.get(
        "/{user_id}",
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
    return get_user_by_user_id_controller.execute(user_id=user_id)