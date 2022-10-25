from typing import Union

from fastapi import FastAPI
from app.models.base import VoteData, Vote, Answer, AnswerData

from app.redis import connect as rb
from app.core.settings import REDIS_HOST, SCHEMA
from app.services.examinations import check_answer_data
import uuid

app = FastAPI()


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(percentage) + "%"


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/")
# async def read_item(item: VoteData):
#     redis = make_redis_connection(REDIS_HOST)
#     answer = await rb.get_value(item.title)
#     data =
#     return {"item_id": item_id, "q": q}

from app.services.make_vote import make_vote_frome_data, make_answer_frome_data
import aioredis


@app.get("/votes/")
async def get_all_votes():
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    data = {}
    async with redis.client() as conn:
        cur = b"0"
        while cur:
            cur, keys = await conn.scan(cur, match="vote:*")
    for key in keys:
        data[key] = await rb.get_value(key)
    return data


@app.post("/votes/")
async def update_item(item: VoteData):
    # values = ",".join(item.options)
    data = make_vote_frome_data(item)
    print("data===", data)
    await rb.set_value(data.id, data.body)
    return data.id


@app.post("/answer/")
async def create_answer(ad: AnswerData):
    check = await check_answer_data(ad)
    answer = make_answer_frome_data(ad)
    if check["status"] == "created":
        await rb.set_value(answer.id, answer.body)
        return await rb.get_value("answer:" + answer.id)
    else:
        return check


@app.get("/answers/")
async def get_answers():
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    data = {}

    async with redis.client() as conn:
        cur = b"0"
        while cur:
            cur, keys = await conn.scan(cur, match="answer:*")
            print("Iteration results:", keys)

    for key in keys:
        data[key] = await rb.get_value(key)
    return data


@app.get("/answers/count/{vote_id}/")
async def get_answers_count(vote_id: str):
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    count_all_voute = 0
    async with redis.client() as conn:
        cur = b"0"
        while cur:
            cur, keys = await conn.scan(cur, match=f"answer:{vote_id}:*")
    vote = await conn.get(f"vote:{vote_id}")
    count_all_voute = len(keys)
    choices = vote.split("|")[1].split(",")
    results = {}
    for x in choices:
        async with redis.client() as conn:
            cur = b"0"
            while cur:
                cur, choice_keys = await conn.scan(cur, match=f"answer:{vote_id}:{x}:*")
        results[x] = percentage(len(choice_keys), count_all_voute)
    return {
        "vote": vote,
        "count": count_all_voute,
        "keys": keys,
        # "count_target_voute": count_target_voute,
        "results": results,
    }
