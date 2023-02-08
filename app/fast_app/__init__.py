from fastapi import FastAPI

from app.config import AppConfig
from app.utils import logger


def create_fast_api() -> FastAPI:
    function_name: str = "Create Fast APP"
    logger.info(function_name=function_name, message=f"Enter - {function_name}")
    app_config: AppConfig = AppConfig()
    fast_app: FastAPI = FastAPI(**app_config.api_kwargs)
    return fast_app


app: FastAPI = create_fast_api()
