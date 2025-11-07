from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship


class OperationEnum(str, PyEnum):
    credit = "credit"
    debit = "debit"


Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    operations = relationship("Operation", back_populates="account")

    def __str__(self):
        """
        Retorna uma string legível e amigável para o usuário.
        """
        return f"Account(id: {self.id}, name: {self.name}, email: {self.email}, operation_ids: {self.operations})"

    def __repr__(self):
        """
        Retorna uma string que pode ser usada para recriar o objeto (idealmente).
        """
        return f"<Account(id={self.id}, name='{self.name}', email='{self.email}')>"


class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    operation = Column(Enum(OperationEnum))
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    account = relationship("Account", back_populates="operations")

    def __str__(self):
        """
        Retorna uma string legível e amigável para o usuário.
        """
        return f"Operation(id: {self.id}, account_id: {self.account_id}, operation: {self.operation.value}, amount: {self.amount}, created_at: {self.created_at})"

    def __repr__(self):
        """
        Retorna uma string que pode ser usada para recriar o objeto (idealmente).
        """
        return f"<Operation(id={self.id}, account_id={self.account_id}, type='{self.operation.value}', amount={self.amount})>"
