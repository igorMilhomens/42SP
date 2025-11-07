FROM python:3.10-slim

WORKDIR /app

COPY api.py ./api.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
