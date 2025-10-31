# Guia rápido:

## Cria o ambiente
python3 -m venv virtual_env 
### ambiente criado no repositorio: /nfs/homes/{usuario}

### Comando para iniciar o ambiente virtual:

source virtual_env/bin/activate # Ativa (Linux)

virtual_env\Scripts\activate.bat # Ativa (Windows)

#### caso a maquina virtual esteja na pasta do seu usuario, basta usar o '~/' como path, ao invés de retornar até a pasta do usuario ex: source ~/virtual_env/bin/activate # Ativa (Linux)


## Evento ex01
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(format_names(persons))


## Evento ex02
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")


## Evento ex03
python3  ex03/convert.py 4
<!-- 4.0 -->

python3 ex03/convert.py hello
<!-- conversion impossible -->


## Evento ex04
python3 ex04/read_file.py ./unknown_file.txt
<!-- Erro: Arquivo não encontrado. -->

python3 ex04/read_file.py /bin/
<!-- Erro: O argumento enviado é um diretório. -->

# cria um arquivo e remove permissões de acesso:
touch ex04/forbidden.txt && chmod 000 ex04/forbidden.txt

python3 ex04/read_file.py ex04/forbidden.txt
<!-- Erro inesperado: PermissionError -->

# cria um arquivo com codificação inválida
echo '\x80abc' > ex04/invalid.txt

python3 ex04/read_file.py ex04/invalid.txt
<!-- Erro inesperado: UnicodeDecodeError -->


## Evento ex05
pytest ex05/test_calculator.py


## Evento ex06
pytest ex06/test_password_validator.py