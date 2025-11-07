#!/bin/bash

# --- Configurações ---
NETWORK_NAME="rede-app-mod-3"
DB_CONTAINER_NAME="postgres-db"
DB_VOLUME_NAME="postgres-data-mod3"
APP_CONTAINER_NAME="42-mod3-aplicacao"
APP_IMAGE_NAME="42-mod3-aplicacao-image"
DB_PASSWORD="ningipoint$2025"
DB_USER="postgres"
DB_NAME="ningipoints"
# ---------------------

# 1. Cria a rede bridge, se ela não existir
echo "Criando/Verificando a rede Docker: $NETWORK_NAME..."
docker network inspect $NETWORK_NAME >/dev/null 2>&1 || docker network create $NETWORK_NAME

# 2. Cria o volume para persistência dos dados do DB, se não existir
echo "Criando/Verificando o volume Docker: $DB_VOLUME_NAME..."
docker volume inspect $DB_VOLUME_NAME >/dev/null 2>&1 || docker volume create $DB_VOLUME_NAME

# Remove containers antigos se ainda estiverem rodando
docker stop $DB_CONTAINER_NAME >/dev/null 2>&1
docker rm $DB_CONTAINER_NAME >/dev/null 2>&1
docker stop $APP_CONTAINER_NAME >/dev/null 2>&1
docker rm $APP_CONTAINER_NAME >/dev/null 2>&1

# 3. Sobe o banco de dados PostgreSQL na rede criada com suas informações
echo "Iniciando o container do banco de dados: $DB_CONTAINER_NAME..."

docker run -d --name $DB_CONTAINER_NAME \
-v $DB_VOLUME_NAME:/var/lib/postgresql/data \
-p 5432:5432 \
-e POSTGRES_DB=$DB_NAME \
-e POSTGRES_USER=$DB_USER \
-e POSTGRES_PASSWORD=$DB_PASSWORD \
--network $NETWORK_NAME \
postgres:13

# 4. Constrói a imagem da sua aplicação (usando o Dockerfile)
echo "Construindo a imagem da aplicação: $APP_IMAGE_NAME..."
docker build -t $APP_IMAGE_NAME .


echo "Aguardando o banco de dados iniciar..."
until docker exec $DB_CONTAINER_NAME pg_isready -U $DB_USER >/dev/null 2>&1; do
  sleep 2
done


# 5. Sobe sua aplicação, conecta à mesma rede e expõe a porta 8080 ao host
echo "Iniciando o container da aplicação: $APP_CONTAINER_NAME na porta 8080..."


docker run -d --name $APP_CONTAINER_NAME \
  --network $NETWORK_NAME \
  -p 8080:8080 \
  $APP_IMAGE_NAME

echo "Configuração concluída. Aplicação em http://localhost:8080"
echo "Host do DB para conexão na aplicação: $DB_CONTAINER_NAME"
