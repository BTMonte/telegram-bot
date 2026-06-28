import asyncpg
from app.core import config

pool = None


async def connect_postgres():
    global pool
    pool = await asyncpg.create_pool(
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        database=config.POSTGRES_DB,
    )
    print("Postgres connected")


async def create_user(telegram_id: int):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO users (telegram_id)
            VALUES ($1)
            ON CONFLICT (telegram_id) DO NOTHING
            """,
            telegram_id
        )


async def get_user(telegram_id: int):
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id = $1",
            telegram_id
        )
