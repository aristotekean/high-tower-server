import os
from pydantic import BaseSettings


class ServerSettings(BaseSettings):
    SERVER_HOST: str = os.environ['SERVER_HOST']
    SERVER_PORT: int = os.environ['SERVER_PORT']

class DatabaseSettings(BaseSettings):
    DB_URL: str = os.environ['DB_URL']
    DB_NAME: str = os.environ['DB_NAME']

class Settings(DatabaseSettings, ServerSettings):
    pass

settings = Settings()
