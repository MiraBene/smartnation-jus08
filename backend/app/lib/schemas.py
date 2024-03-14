import pydantic as pyd


class _Message(pyd.BaseModel):
    content: str


class Answer(_Message):
    pass


class Question(_Message):
    pass
