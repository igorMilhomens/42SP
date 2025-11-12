AWS CLI Command Reference: https://docs.aws.amazon.com/cli/latest/reference/s3api/#available-commands

# Localstack

## Execute:
docker run \
  --rm -it \
  -p 127.0.0.1:4566:4566 \
  -p 127.0.0.1:4510-4559:4510-4559 \
  -v /run/user/$(id -u)/docker.sock:/var/run/docker.sock \
  localstack/localstack

## Execute para carregar as variaveis locais:

source dev.env

# ex01
## Execute os comandos dentro do diretorio 'modulo-3/':
./ex01/create_buckets.sh
./ex01/list_buckets.sh

### caso o arquivo não tenha permissão, erro: "zsh: permission denied: ./ex01/create_buckets.sh" de permissão com o comando:
chmod +x [nome_do_arquivo]

## Comando para excluir bucket:
aws s3api delete-bucket --bucket [nome_do_bucket] --region us-east-1
### aws s3api delete-bucket --bucket 42sp-imilhome-bucket --region us-east-1
### aws s3 rm s3://42sp-imilhome-bucket --recursive --region us-east-1



# ex02
execute os comandos
./ex02/upload_object.sh
./ex02/list_objects.sh
./ex02/download_object.sh
./ex02/remove_object.sh

# ex03
python3 decode.py "42sp-imilhome-bucket" "sample_images/image.txt"

aws s3 cp s3://42sp-imilhome-bucket/image.jpg sample_images/image.jpg


# ex04 
./create_table.sh  
aws dynamodb delete-table --table-name Usuarios --no-cli-pager
aws dynamodb describe-table --table-name Usuarios --no-cli-pager

# ex05
python3 dynamo_crud.py load ./users.csv
python3 dynamo_crud.py retrieve u304
python3 dynamo_crud.py delete u304
python3 dynamo_crud.py update u304 "Novo Nome"

# ex06

python3 dynamo_crud.py load ./use(virtual_env) c1r4p4% python3 dynamo_crud.py load ./users_with_documents.csv Ocorreu um erro durante o carregamento: An error occurred (ResourceNotFoundException) when calling the BatchWriteItem operation: Requested resource not foundrs_with_documents.csv


# ex07

## Carregar as chaves do arquivo prod.env:
source prod.env

## Validar se foram carregados com o comando:
echo $ENV
<!-- resultado deve ser 'prod' -->

## executar o comando de crate do bucket ex1
## Para criar a tabela usar o botão na pagina da AWS

aws dynamodb describe-table --table-name Usuarios > table_info.json


# ex08
python3 presign.py 42sp-imilhome-bucket 28d50f83-b9db-41b9-a900-fe2064e692b2.jpg


# ex09

## Rodar o comando para URL publica
./get-bucket-policy.sh
./put-bucket-policy.sh

## montar URL do OBJETO no formato : https://<bucketname>.s3.amazonaws.com/<objectkey>

https://<bucketname>.s3.amazonaws.com/<objectkey>
s3://42sp-vito-car-bucket/image1.jpg

Abrir em uma guia anonima:
https://42sp-vito-car-bucket.s3.amazonaws.com/image1.jpg


https://<bucketname>.s3.amazonaws.com/<objectkey>
s3://42sp-imilhome-bucket/28d50f83-b9db-41b9-a900-fe2064e692b2.jpg

https://42sp-imilhome-bucket.s3.amazonaws.com/28d50f83-b9db-41b9-a900-fe2064e692b2.jpg