from fastapi import FastAPI

class BootstrapApp:
    _instance: FastAPI | None = None

    @classmethod
    def get(cls) -> FastAPI:
        if cls._instance is None:
            cls._instance = FastAPI()
        return cls._instance