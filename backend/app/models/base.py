from pydantic import BaseModel


class VoteData(BaseModel):
    # id:
    title: str
    options: set[str | int] = set()


class Vote(BaseModel):
    id: str
    body: str  # title|opt,opt,opt


class AnswerData(BaseModel):
    vote_id: str
    choice: str


class Answer(BaseModel):
    id: str
    body: str  # vote_id|choice
