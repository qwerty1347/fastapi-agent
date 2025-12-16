from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOWED_ORIGINS: str | None

    STORAGE_PATH: str
    UPLOAD_PATH: str
    IMAGE_PATH: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()