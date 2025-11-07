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


@pytest.fixture
def account_with_operations_in_database(db_instance):
    """
    Fixture that inserts an account and an operation into the database using a different ID.
    """
    account_data = {
        "id": OPERATION_ACCOUNT_ID,
        "name": "Maria Silva",
        "email": "maria@email.com",
    }
    db_instance.create_account(Account(**account_data))
    operation_data_full = OPERATION_DATA_INPUT.copy()
    operation_data_full["account_id"] = OPERATION_ACCOUNT_ID
    operation_data_full["created_at"] = datetime.now()
    db_instance.create_operation(Operation(**operation_data_full))


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


# --- Tests for POST /accounts/{id}/operations ---


def test_post_account_operation_endpoint_success(account_in_database) -> None:
    """
    Testa o endpoint POST /accounts/{id}/operations, esperando um sucesso (201 Created)
    ao adicionar uma operação a uma conta existente.
    """
    account_id = ACCOUNT_DATA["id"]
    response = client.post(
        f"/accounts/{account_id}/operations", json=OPERATION_DATA_INPUT
    )

    assert response.status_code == 201
    assert response.json()["message"] == "Operação adicionada com sucesso"
    assert response.json()["data"]["operation"] == OPERATION_DATA_INPUT["operation"]
    assert response.json()["data"]["amount"] == OPERATION_DATA_INPUT["amount"]


def test_post_account_operation_endpoint_account_not_found(db_instance) -> None:
    """
    Testa o endpoint POST /accounts/{id}/operations, esperando uma falha (404 Not Found)
    quando a conta de destino não existe.
    """
    non_existent_id = 99999
    response = client.post(
        f"/accounts/{non_existent_id}/operations", json=OPERATION_DATA_INPUT
    )

    assert response.status_code == 404
    assert f"Conta com id {non_existent_id} não encontrada." in response.text


# --- Tests for GET /accounts/{id}/operations ---


def test_get_account_operations_endpoint_success(
    account_with_operations_in_database,
) -> None:
    """
    Testa o endpoint GET /accounts/{id}/operations, esperando um sucesso (200 OK)
    ao listar operações de uma conta existente que possui operações.
    """
    response = client.get(f"/accounts/{OPERATION_ACCOUNT_ID}/operations")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["amount"] == OPERATION_DATA_INPUT["amount"]
    assert response.json()[0]["account_id"] == OPERATION_ACCOUNT_ID


def test_get_account_operations_endpoint_no_content(account_in_database) -> None:
    """
    Testa o endpoint GET /accounts/{id}/operations, esperando um (204 No Content)
    se a conta existe, mas não tem operações.
    """
    account_id = ACCOUNT_DATA["id"]
    response = client.get(f"/accounts/{account_id}/operations")

    assert response.status_code == 204
    assert response.content == b""


def test_get_account_operations_endpoint_account_not_found(db_instance) -> None:
    """
    Testa o endpoint GET /accounts/{id}/operations, esperando uma falha (404 Not Found)
    quando a conta não existe.
    """
    non_existent_id = 99999
    response = client.get(f"/accounts/{non_existent_id}/operations")

    assert response.status_code == 404
    assert f"Conta com id {non_existent_id} não encontrada." in response.text


# --- Tests for DELETE /accounts/{id} ---


def test_delete_account_endpoint_success(account_in_database) -> None:
    """
    Testa o endpoint DELETE /accounts/{id}, esperando um sucesso (204 No Content)
    ao deletar uma conta existente.
    """
    account_id = ACCOUNT_DATA["id"]
    response = client.delete(f"/accounts/{account_id}")

    assert response.status_code == 204
    assert response.content == b""

    # Verify the account is actually gone
    verify_response = client.get(f"/accounts/{account_id}")
    assert verify_response.status_code == 404


def test_delete_account_endpoint_not_found(db_instance) -> None:
    """
    Testa o endpoint DELETE /accounts/{id}, esperando uma falha (404 Not Found)
    quando a conta a ser deletada não existe.
    """
    non_existent_id = 99999
    response = client.delete(f"/accounts/{non_existent_id}")

    assert response.status_code == 404
    assert (
        f"Conta com id {non_existent_id} não encontrada na base de dados."
        in response.text
    )
