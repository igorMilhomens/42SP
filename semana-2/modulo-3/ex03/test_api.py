from datetime import datetime

import pytest
from api import app
from database import DataBase
from fastapi.testclient import TestClient
from models import Account, Operation

client = TestClient(app)

ACCOUNT_DATA = {"id": 12345, "name": "Jose Santos", "email": "jose.Santos@email.com"}
OPERATION_ACCOUNT_ID = 9999
OPERATION_DATA_INPUT = {
    "operation": "credit",
    "amount": 100000,
}


@pytest.fixture
def db_instance():
    """Fixture que garante que a instância do banco de dados esteja acessível e vazia para cada teste."""
    return DataBase()


@pytest.fixture
def account_in_database(db_instance):
    """
    Fixture que insere um registro ACCOUNT_DATA no banco de dados.
    """
    db_instance.create_account(Account(**ACCOUNT_DATA))


# --- Tests for PUT /accounts ---


def test_put_accounts_endpoint(db_instance) -> None:
    """
    Testa o endpoint PUT /accounts, esperando um sucesso (201 Created)
    ao criar um novo registro em um banco de dados vazio.
    """
    response = client.put("/accounts", json=ACCOUNT_DATA)
    assert response.status_code == 201
    assert "application/json" in response.headers["content-type"]
    assert response.json() == ACCOUNT_DATA


def test_put_accounts_endpoint_failure(account_in_database) -> None:
    """
    Testa o endpoint PUT /accounts, esperando uma falha (409 Conflict)
    quando a conta com o mesmo ID já existe.
    """
    response = client.put("/accounts", json=ACCOUNT_DATA)
    expected_error_message = (
        "ID da conta existente. Por favor, verifique os dados e tente novamente."
    )
    assert response.status_code == 409
    assert "application/json" in response.headers["content-type"]
    assert expected_error_message in response.text


# --- Tests for GET /accounts ---


def test_get_accounts_endpoint(account_in_database) -> None:
    """
    Testa o endpoint GET /accounts, esperando um sucesso (200 OK)
    ao retornar os registros existentes.
    """
    response = client.get("/accounts")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == ACCOUNT_DATA["id"]


def test_get_accounts_endpoint_no_content(db_instance) -> None:
    """
    Testa o endpoint GET /accounts quando o banco de dados está vazio,
    esperando um (204 No Content).
    """
    response = client.get("/accounts")
    assert response.status_code == 204
    assert response.content == b""


# --- Tests for GET /accounts/{id} ---


def test_get_accounts_by_id_endpoint(account_in_database) -> None:
    """
    Testa o endpoint GET /accounts/{id}, esperando um sucesso (200 OK)
    ao retornar o registro existente.
    """
    account_id = ACCOUNT_DATA["id"]
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert response.json()["id"] == account_id
    assert response.json()["name"] == ACCOUNT_DATA["name"]


def test_get_accounts_by_id_endpoint_not_found(db_instance) -> None:
    """
    Testa o endpoint GET /accounts/{id}, esperando uma falha (404 Not Found)
    quando a conta não existe.
    """
    account_id = 99999  # A non-existent ID
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 404
    assert "Conta não encontrada na base." in response.text
