import psycopg2
from sqlalchemy import create_engine
from models import Base
import os
from dotenv import load_dotenv, find_dotenv

find_dotenv


def get_psycopg2_connection():
    """Cria e retorna uma nova conexão psycopg2."""
    conn = psycopg2.connect(
        dbname=os.getenv("dbname"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    return conn


def create_tables_if_not_exist():
    try:
        engine = create_engine(
            "postgresql+psycopg2://", creator=get_psycopg2_connection
        )
        Base.metadata.create_all(bind=engine)
        print("Tabelas verificadas e criadas (se necessário) com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar as tabelas: {e}")


if __name__ == "__main__":
    load_dotenv()
    caminho_encontrado = find_dotenv()
    print(f"Diretório de trabalho atual (CWD): {os.getcwd()}")
    if caminho_encontrado:
        print(f"Arquivo .env encontrado em: {caminho_encontrado}")
    else:
        print("find_dotenv() não encontrou o arquivo .env automaticamente.")
    create_tables_if_not_exist()
