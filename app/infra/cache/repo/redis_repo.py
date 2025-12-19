from app.infra.cache.connection import RedisConnection

class RedisRepo:
    def __init__(self, redis_conn: RedisConnection):
        self.__redis_conn = redis_conn

    def set(self, key: str, value: str) -> None:
        self.__redis_conn.set(key, value)

    def get(self, key: str) -> str:
        return (
            self.__redis_conn.get(key).decode("utf-8")
            if self.__redis_conn.get(key) else None
        )

    def delete(self, key: str) -> None:
        self.__redis_conn.delete(key)
    
    def hset(self, hash_name: str, key: str, value: any) -> None:
        self.__redis_conn.hset(hash_name, key, value)

    def hget(self, hash_name: str, key: str) -> str:
        return (
            self.__redis_conn.hget(hash_name, key).decode("utf-8")
            if self.__redis_conn.hget(hash_name, key) else None
        )

    def hdelete(self, hash_name: str, key: str) -> None:
        self.__redis_conn.hdel(hash_name, key)