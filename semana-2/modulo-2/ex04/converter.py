import base64
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

STATIC_PATH = Path(__file__).parent.absolute().joinpath("static")
FORM_HTML = STATIC_PATH.joinpath("form.html").read_text(encoding="utf-8")

app = FastAPI(
    title="Base64 Converter",
    description="Convert text to and from Base64.",
)


@app.post("/encode", response_model=dict[str, str])
def encode_to_base64(request: dict[str, str]) -> dict[str, str]:
    text = request.get("text")
    if not isinstance(text, str):
        raise HTTPException(status_code=422, detail="Field 'text' is required")
    encoded = base64.b64encode(text.encode()).decode()
    return {"text": encoded}


@app.post("/decode", response_model=dict[str, str])
def decode_to_base64(request: dict[str, str]) -> dict[str, str]:
    text = request.get("text")
    if not isinstance(text, str):
        raise HTTPException(status_code=422, detail="Field 'text' is required")
    try:
        decoded = base64.b64decode(text.encode()).decode()
        return {"text": decoded}
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"{e}")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def form() -> str:
    return FORM_HTML


# no main function has been included,
# as the app is intended to be run with uvicorn
# to run, use:
# uvicorn converter:app --reload --reload-include 'static/*.html'
