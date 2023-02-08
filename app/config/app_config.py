from functools import lru_cache
from typing import Dict, Any

from pydantic import BaseSettings

from app.utils.logger import logger


class AppConfig(BaseSettings):
    debug: bool = False
    title: str
    version: str
    description: str

    class Config:
        env_file = ".env"
        validate_assignment = True

    @property
    def api_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
            "description": self.description,
        }


app_config = AppConfig()


@lru_cache()
def generate_settings() -> AppConfig:
    function_desc = "GenerateSettings"
    logger.info(
        function_name=function_desc,
        message=f"Using {app_config.title} Environment Config",
    )
    return AppConfig()
