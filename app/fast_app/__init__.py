from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.config import AppConfig, PATH
from app.fast_app.image_analyser_router import image_analyser_router
from app.schema import CommonResponseSchema
from app.utils import logger


def create_fast_api() -> FastAPI:
    function_name: str = "Create Fast APP"
    logger.info(function_name=function_name, message=f"Enter - {function_name}")
    app_config: AppConfig = AppConfig()
    fast_app: FastAPI = FastAPI(**app_config.api_kwargs)
    return fast_app


app: FastAPI = create_fast_api()


@app.get("/ping", tags=["Health Check"])
def ping():
    function_name: str = "Health Check"
    logger.info(function_name=function_name, message=f"Enter - {function_name}")
    return CommonResponseSchema(
        message="Health check working for Fast App", status="Ok"
    )


app.include_router(image_analyser_router)
app.mount("/static", StaticFiles(directory=PATH), name="static")
