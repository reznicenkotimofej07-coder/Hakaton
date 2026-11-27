from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "LectureAI"
    host: str = "127.0.0.1"
    port: int = 8000

    storage_dir: Path = BASE_DIR / "storage"
    materials_dir: Path = BASE_DIR / "materials"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


settings = Settings()