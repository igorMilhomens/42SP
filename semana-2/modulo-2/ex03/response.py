import sys

import httpx
from httpx import HTTPError

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        result = httpx.get(url)
        print(f"{result.status_code} {result.reason_phrase}")
    except HTTPError as e:
        print(f"Erro: {type(e).__name__}")
