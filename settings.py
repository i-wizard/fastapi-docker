import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    def __new__(self):
        if not hasattr(self, "instance"):
            self.instance = super(Settings, self).__new__(self)
        return self.instance

    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PORT = os.environ.get("POSTGRES_PORT")
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db:{DB_PORT}/{DB_NAME}"


settings = Settings()
