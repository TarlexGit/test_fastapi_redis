import uuid

from app.models.base import VoteData, Vote, AnswerData, Answer


def make_vote_frome_data(vd: VoteData):
    new_id = str(uuid.uuid4())
    opts = ",".join(vd.options)
    body = vd.title + "|" + opts
    v = Vote(id="vote:" + new_id, body=body)
    return v


def make_answer_frome_data(ans: AnswerData) -> Answer:
    new_id = str(uuid.uuid4())
    v = Answer(id=f"answer:{ans.vote_id}:{ans.choice}:{new_id}", body=ans.choice)
    return v
