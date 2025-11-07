from fastapi.testclient import TestClient
from converter import app
import base64

client = TestClient(app)


def test_root_endpoint():
    """
    Test the root endpoint returns HTML
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Base64 Encoder" in response.text


def test_encode_endpoint():
    """
    Test encoding text to Base64
    """
    given = "Hello World"
    expected = base64.b64encode(given.encode()).decode()
    response = client.post("/encode", json={"text": given})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == expected


def test_decode_endpoint():
    """
    Test encoding text to Base64
    """
    given = "SGVsbG8gV29ybGQ="
    expected = base64.b64decode(given.encode()).decode()
    response = client.post("/decode", json={"text": given})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == expected


def test_encode_empty_string():
    """
    Test encoding empty string
    """
    given = ""
    expected = ""
    response = client.post("/encode", json={"text": given})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == expected


def test_decode_empty_string():
    """
    Test encoding empty string
    """
    given = ""
    expected = ""
    response = client.post("/decode", json={"text": given})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == expected
