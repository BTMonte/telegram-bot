import os
from dotenv import load_dotenv

load_dotenv()


def get_env(name: str, default=None):
    value = os.getenv(name)
    return value if value is not None else default


def get_int_env(name: str, default=None):
    value = os.getenv(name)
    return int(value) if value is not None else default


# ENV (local / prod)
ENV = get_env("ENV", "local")

# Telegram
BOT_TOKEN = get_env("BOT_TOKEN")


# Postgres
DB_HOST = get_env("DB_HOST")
DB_PORT = get_int_env("DB_PORT", 5432)
DB_NAME = get_env("DB_NAME")
DB_USER = get_env("DB_USER")
DB_PASSWORD = get_env("DB_PASSWORD")


# Redis
REDIS_HOST = get_env("REDIS_HOST")
REDIS_PORT = get_int_env("REDIS_PORT", 6379)