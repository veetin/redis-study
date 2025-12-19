import redis

from configs import settings


class RedisConnection:
    def __init__(self):
        self.__host = settings.redis_host
        self.__port = settings.redis_port
        self.__db = settings.redis_db
        self.__connection = None

    def connect(self):
        self.__connection = redis.Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db,
        )
        return self.__connection

    def get_connection(self):
        return self.__connection
