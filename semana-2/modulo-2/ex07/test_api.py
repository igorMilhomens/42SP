from api import app
from fastapi.testclient import TestClient

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
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]
    assert "Input should be a valid dictionary" in response.text


def test_post_create_endpoint_failure() -> None:
    """
    Test the root endpoint returns post
    """
    expected = {"foo": "bar"}
    response = client.post("/create", json=expected)
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]
    assert '{"foo":"bar"}' in response.text


def test_post_create_endpoint_success() -> None:
    """
    Test the root endpoint returns post
    """
    expected = {'name': 'Osvaldo',
        'age': 45,
        'email': 'osvaldo@os.com',
        'balance': 10_000_00
    }
    response = client.post("/create", json=expected)
    assert response.status_code == 201
    assert "application/json" in response.headers["content-type"]
    assert '{"name":"Osvaldo","age":45,"email":"osvaldo@os.com","balance":1000000}' in response.text


def test_post_create_endpoint_failure_email() -> None:
    """
    Test the root endpoint returns post
    """
    expected = {'name': 'Osvaldo',
        'age': 45,
        'email': 'osvaldo',
        'balance': 10_000_00
    }
    response = client.post("/create", json=expected)
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]
    assert '{"reason":"An email address must have an @-sign."}' in response.text


def test_post_create_endpoint_failure_name_length() -> None:
    """
    Test the root endpoint returns post
    """
    expected = {'name': 'Osvaldo Silva Antunes Ferreira Cardoso Neves Oliveira',
        'age': 45,
        'email': 'osvaldo@email.com',
        'balance': 10_000_00
    }
    response = client.post("/create", json=expected)
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]
    assert '"msg":"String should have at most 50 characters"' in response.text