FROM python:3.10-slim

COPY public/ ./public/
ENTRYPOINT [ "python3" ,"-m",  "http.server"]

CMD ["8080", "-d", "/public/"]