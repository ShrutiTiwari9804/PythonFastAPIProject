import os
from dotenv import load_dotenv
# from pydantic_settings import BaseSettings

load_dotenv()

class Settings():
    SECRET_KEY = os.getenv("SECRET_KEY")
    origins = [
        os.getenv("ORIGINS")
    ]
    DB_URL = os.getenv("DB_URL")


settings = Settings()

