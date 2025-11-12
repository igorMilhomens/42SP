#! /bin/bash

echo "Criando a tabela DynamoDb..."

aws dynamodb create-table \
    --table-name Usuarios \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --no-cli-pager

echo "Aguardando a tabela estar ativa..."

aws dynamodb wait table-exists --table-name Usuarios

echo "Tabela criada com sucesso."