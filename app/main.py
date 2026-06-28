import asyncio
from app.db.postgres import connect_postgres, create_user, get_user


async def main():
    print("Backend test started")

    await connect_postgres()

    print("Creating user...")

    await create_user(777)

    user = await get_user(777)

    print("User from DB:", user)


if __name__ == "__main__":
    asyncio.run(main())
