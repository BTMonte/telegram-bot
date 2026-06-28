from app.db.postgres import fetch_one


async def get_user(user_id: int):
    return await fetch_one(
        "SELECT $1 as user_id",
        user_id
    )
