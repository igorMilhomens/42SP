from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import declarative_base


class OperationEnum(str, PyEnum):
    credit = "credit"
    debit = "debit"


Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    operation = Column(Enum(OperationEnum))
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
