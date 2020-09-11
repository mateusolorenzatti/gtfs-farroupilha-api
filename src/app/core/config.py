
from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator

from decouple import config

class Settings(BaseSettings):

    PROJECT_NAME: str = "GTFS Farroupilha API"

    API_BASE_ROUTE: str = "/api/v1"

    #Importar para aquivo .env
    POSTGRES_SERVER: str = config('POSTGRES_SERVER')
    POSTGRES_USER: str = config('POSTGRES_USER')
    POSTGRES_PASSWORD: str = config('POSTGRES_PASSWORD')
    POSTGRES_DB: str = config('POSTGRES_DB')

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

settings = Settings()