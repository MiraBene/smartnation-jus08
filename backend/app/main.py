from typing import List

import fastapi

from . import schemas
from . import services


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
async def fetch_position(form_data: schemas.Question = fastapi.Depends()):
    print(form_data)

    return services.get_answer_from_chat(form_data.content)
