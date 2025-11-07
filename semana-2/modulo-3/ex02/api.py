from database import DataBase
from fastapi import FastAPI, HTTPException, status
from models import Account as ModelAccount
from schemas import AccountCreate as SchemaAccount, OperationCreate as SchemaOperation
from sqlalchemy.exc import IntegrityError


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
