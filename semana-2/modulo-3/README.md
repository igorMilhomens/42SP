#  VALIDAÇÃO

## Inicio

verifique se a containers e imagens criadas na maquina

### Para verificar se existem containers em execução 
docker ps 
### Caso exista container em execução, finalize a execução:
docker stop {nome_do_container}

### Para verificar os containers existentes use 
docker ps -a

### Para verificar as imagens existentes use 
docker images

Exclua os containers executando na maquina para evitar conflitos

docker rm  # use 'tab' para completar o comando
ex.: docker rm postgres

### Parte do comando    | Descriçãodocker run --name postgres \
docker                  | O comando principal da interface de linha de comando (CLI) do Docker.
rm                      | Subcomando para "remove" (remover). Especificamente, ele remove um ou mais contêineres (e não a imagem ou volumes, a menos que especificado com opções adicionais).
postgres                | O nome ou o ID do contêiner específico que se deseja remover. Neste caso, refere-se ao contêiner chamado postgres.

Também exclua as imagens

docker rmi  # use 'tab' para completar o comando
ex.: docker rmi postgres

==============================================================================================================================================

# EX01

## execute o comando para criar a variavel de ambiente om a senha do :

export POSTGRES_PASSWORD='ningipoint$2025'

# Comando para criar a instancia do postgres ajustado
docker run --name postgres \
-v postgres-data:/var/lib/postgresql \
-p 5432:5432 \
-e POSTGRES_DB=ningipoints \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
-d postgres


ou use o comando direto:

docker run --name postgres \
-v postgres-data:/var/lib/postgresql \
-p 5432:5432 \
-e POSTGRES_DB=ningipoints \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD='ningipoint$2025' \
-d postgres

## Parte do comando                     | Descrição
docker run                              | Cria e inicia um novo container a partir de uma imagem.
--name postgres                         | Atribui o nome postgres ao container.
-v postgres-data:/var/lib/postgresql    | Volume: Mapeia o volume do Docker postgres-data para o diretório /var/lib/postgresql dentro do container, garantindo a persistência dos dados do banco.
-p 5432:5432                            | Mapeia a porta 5432 do host para a porta 5432 do container.
-e POSTGRES_DB                          | Variável de Ambiente: Define variáveis de ambiente dentro do container para configuração, como nome do DB, usuário e senha.
-d                                      | Detach mode: Executa o container em segundo plano (backgrounddireto).
postgres                                | O nome da imagem Docker a ser utilizada.

## Rode a aplicação com o comando, seu terminal precisa estar na raiz do projeto:

python3 ex01/build_tables.py


## Valide a criação da tabela, é possivel usar a extensao PostgreSQL no visual studio
Connection Parameters
Server name*
    127.0.0.1
Authentication Type*
    Password
User name*
    postgres
Password
    ningipoint$2025
Database name
    ningipoints
Connection Name
    postgres

==============================================================================================================================================

# EX02

## Crie a conexão com o uvicorn, entre na pasta do exercicio ex02 e execute o comando:

uvicorn api:app

## acesse o ip disponibilizado e adicione o /docs ex:

http://127.0.0.1:8000/docs

Valide os Endpoints conforme necessidade

==============================================================================================================================================
# EX03

## Crie a conexão com o uvicorn, entre na pasta do exercicio ex03 e execute o comando:

uvicorn api:app

## acesse o ip disponibilizado e adicione o /docs ex:

http://127.0.0.1:8000/docs

Valide os Endpoints conforme necessidade

==============================================================================================================================================
# EX04

## Crie a conexão com o uvicorn, entre na pasta do exercicio ex04 e execute o comando:

uvicorn api:app

## acesse o ip disponibilizado e adicione o /docs ex:

http://127.0.0.1:8000/docs

Valide os Endpoints conforme necessidade

==============================================================================================================================================
# EX05

## Crie a conexão com o uvicorn, entre na pasta do exercicio ex05 e execute o comando:

uvicorn api:app

## acesse o ip disponibilizado e adicione o /docs ex:

http://127.0.0.1:8000/docs

Valide os Endpoints conforme necessidade

==============================================================================================================================================

# EX06


## Execute o comando:

chmod +x run.sh

## em seguida:

./run.sh 



==============================================================================================================================================