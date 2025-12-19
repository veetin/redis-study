from app.infra.cache.connection import RedisConnection
from app.infra.cache.repo.redis_repo import RedisRepo

redis_conn = RedisConnection().connect()
redis_repo = RedisRepo(redis_conn)


def get_redis_conn() -> RedisConnection:
    return redis_conn


def get_redis_repo() -> RedisRepo:
    return redis_repo
