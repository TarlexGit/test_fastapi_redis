import aioredis


async def make_redis_connection(host):
    try:
        redis = await aioredis.from_url(host)
        return redis
    except Exception as err:
        print(err)
        return None


async def set_value(conn, key, value):
    try:
        await conn.set("key:" + key, value)
    except Exception as err:
        print(err)  # TODO logging
        return "err"


async def get_value(conn, value):
    try:
        value = await conn.get(value)
        return value
    except Exception as err:
        print(err)  # TODO logging
        return "err"


# class RedisBox:
#     # __slots__ = ["redis"]

#     def __init__(self, redis) -> None:
#         self.redis = make_redis_connection(redis)


async def set_value(key, value):
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    async with redis.client() as conn:
        await conn.set(key, value)


async def get_value(value):
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    async with redis.client() as conn:
        val = await conn.get(value)
    return val

    # def __del__(self):
    #     self.redis.close()
