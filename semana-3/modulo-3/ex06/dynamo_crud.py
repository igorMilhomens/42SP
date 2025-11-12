import sys
import csv
from typing import Any
import boto3
from botocore.exceptions import ClientError
from decode import decode_image, upload_image_s3
import uuid

def load_users(table: Any, csv_file_path: str) -> None:
    """Carrega dados de usuários de um arquivo CSV para a tabela do DynamoDB."""
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            with table.batch_writer() as batch:
                for row in reader:
                    hash = f"{uuid.uuid4()}.jpg"
                    item = {
                        'id': row['id'],
                        'name': row['name'],
                        'document_key': hash
                    }
                    batch.put_item(Item=item)

                    image_bytes = decode_image(row['document'])
                    upload_image_s3(image_bytes,hash)
        
        print(f"Carregando dados de'{csv_file_path}'")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{csv_file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante o carregamento: {e}")
    

def retrieve_user(table: Any, user_id: str) -> None:
    """Recupera e exibe um usuário específico pelo ID."""
    try:
        response = table.get_item(Key={'id': user_id})
        item = response.get('Item')
        if item:
            print(f"Usuário encontrado: {item}")
        else:
            print(f"Usuário com ID '{user_id}' não encontrado.")
    except ClientError as e:
        print(f"Erro ao recuperar usuário: {e.response['Error']['Message']}")

    

def update_user(table: Any, user_id: str, new_name: str) -> None:
    """Atualiza o atributo 'name' de um usuário existente."""
    try:
        table.update_item(
            Key={'id': user_id},
            UpdateExpression="set #n = :val1",
            ExpressionAttributeNames={'#n': 'name'},
            ExpressionAttributeValues={':val1': new_name},
            ReturnValues="UPDATED_NEW"
        )
        print(f"Usuário {user_id} atualizado para o nome - '{new_name}'")
    except ClientError as e:
        print(f"Erro ao atualizar usuário: {e.response['Error']['Message']}")

def delete_user(table: Any, user_id: str) -> None:
    """Exclui um usuário específico pelo ID."""
    try:
        table.delete_item(
            Key={'id': user_id}
        )
        print(f"Usuário {user_id} removido")
    except ClientError as e:
        print(f"Erro ao excluir usuário: {e.response['Error']['Message']}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python seu_script.py <acao> <parametro1> [parametro2]")
        print("Exemplo: python seu_script.py load usuarios.csv")
        print("Exemplo: python seu_script.py retrieve u448")
        print("Exemplo: python seu_script.py update u448 'Novo Nome'")
        print("Exemplo: python seu_script.py delete u448")
        sys.exit(1)
    action = sys.argv[1]
    param1 = sys.argv[2]
    param2 = sys.argv[3] if len(sys.argv) > 3 else None
    csv.field_size_limit(sys.maxsize)
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Usuarios')

    match action:
        case 'load':
            load_users(table, param1)
        case 'retrieve':
            retrieve_user(table, param1)
        case 'update':
            if param2:
                update_user(table, param1, param2)
            else:
                print("Erro: Ação 'update' requer um novo nome como segundo parâmetro.")
        case 'delete':
            delete_user(table, param1)
        case _:
            print(f"Ação '{action}' desconhecida.")

