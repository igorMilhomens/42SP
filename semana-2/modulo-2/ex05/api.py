import sys
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# from fastapi.responses import HTMLResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse("json em formato invalido.", status_code=400)


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
