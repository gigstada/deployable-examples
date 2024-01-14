from typing import Union

from fastapi import FastAPI

from dotenv import load_dotenv

import os

load_dotenv()

app = FastAPI()

SOME_ENV_VAR = os.getenv("SOME_ENV_VAR")


@app.get("/")
def read_root():
    return {"Hello": "World!", "SOME_ENV_VAR": SOME_ENV_VAR}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
