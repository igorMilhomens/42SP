import httpx
from httpx import Response

def do_GET() -> str:
    result = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
    # text = result.text.replace('\n', ' ')
    return f"{result.status_code} {result.text}"

def do_POST() -> str:
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1
        }

    result = httpx.post("https://jsonplaceholder.typicode.com/posts", data=body) 
    return f"{result.status_code} {result.text}"

def main() -> None:
    print(do_GET())
    print(do_POST())

if __name__ == "__main__":
    main()