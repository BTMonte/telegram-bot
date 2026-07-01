import asyncpg
from app.core import config

pool = None


async def connect_postgres():
    global pool
    pool = await asyncpg.create_pool(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
    )
    print("Postgres connected")


async def fetch_one(query: str, *args):
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, *args)


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

async def close_postgres():
    global pool
    if pool is not None:
        await pool.close()
        pool = None
        print("Postgres disconnected")
