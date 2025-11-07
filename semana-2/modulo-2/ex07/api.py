import sys
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field


# from fastapi.responses import HTMLResponse
class Account(BaseModel):
    name: str = Field(max_length=50)
    age: int 
    email: EmailStr
    balance: int


app = FastAPI()


@app.get("/", response_model=dict[str, str])
def get_root() -> dict[str, str]:
    return {"message": "Bem-vindo à minha API!"}


@app.post("/")
def post_root(request: dict[str, str]) -> JSONResponse:
    if request:
        return JSONResponse(request, status_code=201)
    raise HTTPException(status_code=400, detail="json em formato invalido.")


@app.get("/info")
def get_info() -> dict[str, str]:
    return {"now": str(datetime.now()), "version": sys.version}


@app.post("/create")
def post_create(account: Account) -> JSONResponse:
    return JSONResponse(account.model_dump(), status_code=201)
