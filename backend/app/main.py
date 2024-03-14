from typing import List

import fastapi

from lib import schemas
from lib import services
from lib.manager import AnswerManager


# Initialise app (and create database if needed)
# ---------------------------------
app = fastapi.FastAPI()


# Routes
# ---------------------------------
@app.get("/info")
async def root():
    """Provide basic information on the API status."""
    return services.get_api_info()


@app.post("/get_answer", response_model=schemas.Answer)
async def fetch_position(query: schemas.Question):
    question = query.content
    manager = AnswerManager()
    orchestrator = manager.build_orchestrator()
    orchestrator.run(question=question)
    if orchestrator.is_success() or orchestrator.result is None:
        print("to the question: ")
        print(question)
        print()
        print("our answer is:")
        print(orchestrator.result)
        return schemas.Answer(content=orchestrator.result)
    else: 
        return schemas.Answer(content="We were unable to answer to your question, sorry :(")

