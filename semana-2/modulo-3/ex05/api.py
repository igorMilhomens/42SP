from database import DataBase
from fastapi import FastAPI, HTTPException, status, Response
from models import Account as ModelAccount, Operation as ModelOperation
from schemas import AccountCreate as SchemaAccount, OperationCreate as SchemaOperation, AccountOperation as SchemaAccountOperation
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


@app.post("/accounts/{id}/operations", status_code=status.HTTP_201_CREATED)
def add_account_operation(id: int, operation_data: SchemaOperation):
    """
    Endpoint (POST) para adicionar uma nova operação a uma conta existente.

    Retorna:
    - 201 Created: Em caso de sucesso ao adicionar a operação.
    - 404 Not Found: Se a conta com o ID especificado não existir.
    """
    account = db_instance.get_account_by_id(id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conta com id {id} não encontrada.",
        )
    operation_data_for_db = operation_data.model_dump()
    operation_data_for_db["account_id"] = id
    new_operation = db_instance.create_operation(
        ModelOperation(**operation_data_for_db)
    )
    return {
        "message": "Operação adicionada com sucesso",
        "data": new_operation,
    }


@app.get("/accounts/{id}/operations")
def get_account_operations(id: int):
    """
    Endpoint (GET) para listar todas as operações de uma conta específica.

    Retorna:
    - 200 OK: Em caso de sucesso, com a lista de operações.
    - 204 No Content: Se a conta existe, mas não possui operações cadastradas.
    - 404 Not Found: Se a conta com o ID especificado não existir.
    """
    account = db_instance.get_account_by_id(id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conta com id {id} não encontrada.",
        )
    operations = db_instance.list_operations_for_account(id)
    if operations:
        return operations
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete("/accounts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account_by_id(id: int):
    """
    Endpoint (DELETE) para remover uma conta e todas as suas operações associadas.

    Retorna:
    - 204 No Content: Se a conta foi deletada com sucesso (ou se já não existia antes).
    - 404 Not Found: Se a conta com o ID especificado não for encontrada.
    """
    account_obj = db_instance.get_account_by_id(id)
    if not account_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conta com id {id} não encontrada na base de dados.",
        )

    db_instance.delete_account(account_obj)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
