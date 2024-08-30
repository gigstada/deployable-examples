from typing import Union
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from typing import Annotated
import os

load_dotenv()

# Main FastAPI app
app = FastAPI()

# Define security
security = HTTPBasic()

# Get credentials from environment variables
LOGIN_USERNAME = os.getenv("LOGIN_USERNAME")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")


# Function to validate username and password
def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = LOGIN_USERNAME.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = LOGIN_PASSWORD.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


# API route group
api_app = FastAPI()


@api_app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: Union[str, None] = None,
    credentials: Annotated[HTTPBasicCredentials, Depends(get_current_username)] = None,
):
    return {"item_id": item_id, "q": q}


# Include the API app under the /api path
app.mount("/api", api_app)

# Mount the static files directory to serve the root path
app.mount("/", StaticFiles(directory="static", html=True), name="static")
