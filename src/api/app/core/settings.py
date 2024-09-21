import os
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = os.getenv('APP_NAME', 'my-app')
    app_version: str = os.getenv('APP_VERSION', '0.0.1')

    app_description: str

    log_level: str = os.getenv('LOG_LEVEL', 'DEBUG')


settings = Settings(
    app_description=(Path(__file__).parent.parent /
                     'static/docs.md').read_text(encoding='utf-8')
)
