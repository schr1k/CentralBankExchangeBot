from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Telegram
    TOKEN: str

    # Redis
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
