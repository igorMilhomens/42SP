from database import DataBase
from fastapi import FastAPI, HTTPException, status, Response
from models import Account as ModelAccount
from schemas import AccountCreate as SchemaAccount,  AccountOperation as SchemaAccountOperation
from sqlalchemy.exc import IntegrityError
from typing import List

app = FastAPI()
db_instance = DataBase()


@app.put("/accounts", response_model=SchemaAccount, status_code=status.HTTP_201_CREATED)
def put_account(account_data: SchemaAccount) -> SchemaAccount:
    """
    Endpoint (PUT) para criar uma conta.

    Retorna:
    - 201 Created: Em caso de sucesso na criação da conta.
    - 409 Conflict: Caso a conta (ID) já exista na base de dados.
    """
    try:
        new_account = db_instance.create_account(
            ModelAccount(**account_data.model_dump())
        )
        return new_account
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ID da conta existente. Por favor, verifique os dados e tente novamente.",
        )


@app.get("/accounts", response_model=List[SchemaAccount])
def get_accounts():
    """
    Endpoint (GET) para retornar uma lista de contas.

    Retorna:
    - 200 OK: Em caso de sucesso, com a lista de contas no corpo da resposta.
    - 204 No Content: Caso não existam contas cadastradas na base.
    """
    response_accounts = db_instance.list_all_accounts()
    if response_accounts:
        return response_accounts
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/accounts/{id}", response_model=SchemaAccountOperation)
def get_accounts_by_id(id: int):
    """
    Endpoint (GET) para retornar uma conta específica e suas operações.
    O 'id' na URL identifica o recurso da conta.

    Retorna:
    - 200 OK: Em caso de sucesso, com os dados da conta e operações.
    - 404 Not Found: Caso a conta com o ID especificado não seja encontrada.
    """
    response = db_instance.get_account_by_id(id)
    if response:
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta não encontrada na base.",
        )