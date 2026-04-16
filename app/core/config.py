from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "marketplace-analytics"

    # Server settings
    host: str = "localhost"
    port: int = 8080


settings = Settings()
