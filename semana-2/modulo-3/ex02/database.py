import os
from datetime import datetime

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
