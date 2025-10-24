from bootstraps.fast_api import BootstrapApp
from infrastructure.routes.users import UsersRouter

app = BootstrapApp.get()

app.include_router(
    UsersRouter,
    prefix="/users",
    tags=["users"]
)
