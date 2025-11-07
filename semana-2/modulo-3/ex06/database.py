import os

import psycopg2
from dotenv import find_dotenv, load_dotenv
from models import Account, Base, Operation
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker


class DataBase:
    def __init__(self):
        self.__load_environment_variables()
        self.engine = create_engine(
            "postgresql+psycopg2://", creator=self.__get_psycopg2_connection
        )
        self.__drop_all_tables()
        self.__create_tables_if_not_exist()
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def mock_init(self):
        """Cria e retorna uma nova conexão psycopg2."""
        self.create_account(
            Account(id=123, name="Jose Santos", email="jose.Santos@email.com")
        )
        self.create_account(
            Account(id=456, name="Jose Souza", email="jose.Souza@email.com")
        )
        self.create_account(
            Account(id=789, name="Jose Sanches", email="jose.Sanches@email.com")
        )
        self.create_operation(
            Operation(
                account_id=123,
                operation="credit",
                amount=100000,
            )
        )

    @staticmethod
    def __get_psycopg2_connection():
        """Cria e retorna uma nova conexão psycopg2."""
        conn = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
        )
        return conn

    @staticmethod
    def __load_environment_variables():
        load_dotenv()
        caminho_encontrado = find_dotenv()
        print(f"Diretório de trabalho atual (CWD): {os.getcwd()}")
        if caminho_encontrado:
            print(f"Arquivo .env encontrado em: {caminho_encontrado}")
        else:
            print("find_dotenv() não encontrou o arquivo .env automaticamente.")

    def __create_tables_if_not_exist(self):
        try:
            Base.metadata.create_all(bind=self.engine)
            print("Todas as tabelas foram criadas com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas: {e}")

    def __drop_all_tables(self):
        """Deleta todas as tabelas mapeadas pelo Base do banco de dados."""
        print("Deletando todas as tabelas existentes...")
        try:
            Base.metadata.drop_all(bind=self.engine)
            print("Tabelas deletadas.")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar as tabelas: {e}")

    def create_account(self, new_account: Account) -> Account:
        """
        Insere uma nova conta no banco de dados. (Funciona como um INSERT)
        Retorna o objeto Account criado.
        """
        with self.SessionLocal() as session:
            session.add(new_account)
            session.commit()
            session.refresh(new_account)
        return new_account

    def list_all_accounts(self) -> list[Account]:
        """
        Retorna uma lista de objetos Account se encontrado, caso contrário retorna None.
        """
        with self.SessionLocal() as session:
            accounts = session.query(Account).all()
            return accounts

    def get_account_by_id(self, account_id: str) -> Account:
        """
        Busca uma conta pelo ID.
        Retorna o objeto Account se encontrado, caso contrário retorna None.
        """
        with self.SessionLocal() as session:
            account = (
                session.query(Account)
                .filter(Account.id == account_id)
                .options(joinedload(Account.operations))
                .first()
            )
            return account

    def create_operation(self, new_operation: Operation) -> Operation:
        """
        Insere uma nova operação no banco de dados. (Funciona como um INSERT)
        O objeto Operation deve ter o account_id já definido.
        """
        with self.SessionLocal() as session:
            session.add(new_operation)
            session.commit()
            session.refresh(new_operation)
        return new_operation

    def list_operations_for_account(self, account_id: int) -> list[Operation]:
        """
        Lista todas as operações para um dado account_id.
        """
        with self.SessionLocal() as session:
            operations = (
                session.query(Operation)
                .filter(Operation.account_id == account_id)
                .all()
            )
            return operations

    def delete_account(self, account: Account) -> None:
        """
        Deleta uma conta existente.
        Retorna True se a conta foi deletada com sucesso, False se não foi encontrada.
        """
        with self.SessionLocal() as session:
            session.query(Operation).filter(Operation.account_id == account.id).delete(
                synchronize_session=False
            )
            session.delete(account)
            session.commit()
