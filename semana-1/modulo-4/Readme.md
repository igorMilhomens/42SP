# Guia rápido:

## Cria o ambiente
python3 -m venv virtual_env 
### ambiente criado no repositorio: /nfs/homes/{usuario}

### Comando para iniciar o ambiente virtual:

source virtual_env/bin/activate # Ativa (Linux)

virtual_env\Scripts\activate.bat # Ativa (Windows)

#### caso a maquina virtual esteja na pasta do seu usuario, basta usar o '~/' como path, ao invés de retornar até a pasta do usuario ex: source ~/virtual_env/bin/activate # Ativa (Linux)


## Evento ex01
>>> import utils
>>> print(utils.format_cents(11_222_00))
[+] R$ 11.222,00


## Evento ex02
>>> import utils
>>> print(utils.format_cents(11_222_00))
[+] R$ 11.222,00
>>> import utils
>>> print(utils.format_cents(11_222_00))
[+] R$ 11.222,00


## Evento ex03
>>> t = Operation(11_222_00, 'ATM deposit')
>>> t
Operation(cents=1122200, operation_type='credit', description='ATM deposit')

>>> print(t)
[+] R$ 11.222,00 (ATM deposit)


## Evento ex04
>>> ac = Account(123, '123.456.789-01')
>>> ac
Account(123, '123.456.789-01')
>>> print(ac)
Account: 123
Balance: [+] R$ 0,00
>>> ac.deposit(1122200, 'ATM deposit')
>>> ac.statement()
[+] R$ 11.222,00 (ATM deposit)
Balance: [+] R$ 11.222,00

## Evento ex05



## Evento ex06
