from pydantic import BaseModel, EmailStr
from models import OperationEnum


class AccountCreate(BaseModel):
    id: int
    name: str
    email: EmailStr


class OperationCreate(BaseModel):
    operation: OperationEnum
    amount: int
