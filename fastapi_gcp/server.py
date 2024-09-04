from typing import Union
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from typing import Annotated
import os

load_dotenv()


# Main FastAPI app with global dependency for authentication
app = FastAPI()


# API route group
api_app = FastAPI()


@api_app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: Union[str, None] = None,
):
    return {"item_id": item_id, "q": q}


# Include the API app under the /api path
app.mount("/api", api_app)

# Mount the static files directory to serve the root path
app.mount("/", StaticFiles(directory="static", html=True), name="static")
