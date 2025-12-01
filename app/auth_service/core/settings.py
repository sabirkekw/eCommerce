from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    app_name: str = "HotelReservationAPI v0.1"
    secret_key: str
    algorithm: str
    token_ttl: int

    class Config:
        """Pydantic configuration."""

        env_file = ".env"


settings = Settings()