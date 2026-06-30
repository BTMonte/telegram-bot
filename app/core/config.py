import os
from dotenv import load_dotenv

load_dotenv()


def get_env(*names: str) -> str | None:
    for name in names:
        value = os.getenv(name)
        if value is not None:
            return value
    return None


def get_int_env(*names: str) -> int | None:
    value = get_env(*names)
    return int(value) if value is not None else None


DB_HOST = get_env("DB_HOST")
DB_PORT = get_int_env("DB_PORT")
DB_NAME = get_env("DB_NAME")
DB_USER = get_env("DB_USER")
DB_PASSWORD = get_env("DB_PASSWORD")

REDIS_HOST = get_env("REDIS_HOST")
REDIS_PORT = get_int_env("REDIS_PORT")
