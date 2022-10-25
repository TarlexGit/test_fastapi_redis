from app.redis import connect as rb
from app.models.base import AnswerData


async def check_answer_data(answer: AnswerData):
    vote = await rb.get_value("vote:" + answer.vote_id)
    print("CHECK vote:", vote)
    print("answer.choice:", answer.choice)
    print("vote.split()[1]", vote.split("|")[1])
    if vote and answer.choice in vote.split("|")[1]:
        return {"status": "created"}
    else:
        return {
            "status": "not created",
            "your choice": answer.choice,
            f"available options to choose for {answer.vote_id}": vote.split("|")[1],
        }
