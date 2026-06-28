import redis
from app.core import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True
)


def ping_redis():
    return redis_client.ping()
