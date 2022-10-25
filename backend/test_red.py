# import asyncio

# import aioredis


# async def main():
#     # redis = aioredis.from_url("redis://127.0.0.1", decode_responses=True)
#     redis = await aioredis.from_url("redis://localhost")
#     async with redis.pipeline(transaction=True) as pipe:
#         ok1, ok2 = await (pipe.set("key1", "value1").set("key2", "value2").execute())
#     print(ok1)
#     assert ok1
#     assert ok2


# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio

import aioredis


async def main():
    """Scan command example."""
    redis = aioredis.from_url("redis://localhost")

    await redis.mset({"key:1": "value1", "key:2": "value2"})
    async with redis.client() as conn:
        cur = b"0"  # set initial cursor to 0
        while cur:
            cur, keys = await conn.scan(cur, match="key:*")

            print("Iteration results:", keys, "\ncur:", cur)
        a_keys = await conn.keys()
        print("all keys:", a_keys)
        print("key:1", await conn.get("key:1"))


if __name__ == "__main__":
    import os

    if "redis_version:2.6" not in os.environ.get("REDIS_VERSION", ""):
        asyncio.run(main())
