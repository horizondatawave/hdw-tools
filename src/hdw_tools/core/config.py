from pydantic_settings import BaseSettings


class Config(BaseSettings):
    HDW_API_URL: str = "https://api.horizondatawave.ai/api"
    HDW_API_KEY: str
