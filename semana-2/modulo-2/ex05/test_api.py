from fastapi.testclient import TestClient

from .api import app

client = TestClient(app)


def test_root_endpoint() -> None:
    """
    Test the root endpoint returns HTML
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert "Bem-vindo à minha API!" in response.text


def test_root_post_endpoint() -> None:
    """
    Test the root endpoint returns post
    """
    expected = {"foo": "bar"}
    response = client.post("/", json=expected)
    assert response.status_code == 201
    assert "application/json" in response.headers["content-type"]
    assert '{"foo":"bar"}' in response.text


def test_root_post_with_empty_json() -> None:
    """
    Test the root endpoint returns post
    """
    response = client.post("/", json={})
    assert response.status_code == 400
    assert "application/json" in response.headers["content-type"]
    assert "json em formato invalido." in response.text


def test_root_post_with_invalid_json() -> None:
    """
    Test the root endpoint returns post
    """
    response = client.post("/", json='{foo:"bar"}')
    assert response.status_code == 400
    assert "application/json" in response.headers["content-type"]
    assert "json em formato invalido." in response.text
