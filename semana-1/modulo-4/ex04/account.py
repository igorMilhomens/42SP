from operation import Operation
from utils import format_cents


class Account:
    """Representa uma conta."""

    def __init__(self, account_id: int, cpf: str):
        """Inicializa um novo objeto Conta.

        Args:
            account_id (int): O nome da pessoa.
            cpf (str): A idade da pessoa.
            __balance (int): A idade da pessoa.
            __operations (str): A idade da pessoa.
        """
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations: list[str] = []

    def __str__(self) -> str:
        """Retorna uma string amigável para o usuário quando o objeto é impresso."""
        return (
            f"Account: {self.account_id}\nBalance: [+] {format_cents(self.__balance)}"
        )

    def __repr__(self) -> str:
        """Retorna a representação oficial do objeto,seguindo o formato:
        Account(account_id, cpf)
        """
        return f"Account({self.account_id}, '{self.cpf}')"

    def deposit(self, amount: int, description: str) -> None:
        """Realiza um depósito na conta, aumentando o saldo.
        O valor é dado em centavos.
        """
        self.__validate_positive_amount(amount)
        op = Operation(amount, description)
        self.__update_operations(str(op))
        self.__update_balance(op.cents)

    def withdraw(self, amount: int, description: str) -> None:
        """Realiza um saque da conta, diminuindo o saldo."""
        self.__validate_positive_amount(amount)
        if amount > self.__balance:
            print(
                "Operação não realizada, valor solicitado para saque é maior que o saldo da conta."
            )
        else:
            value_withdrawal = amount * (-1)
            op = Operation(value_withdrawal, description)
            self.__update_operations(str(op))
            self.__update_balance(op.cents)

    def statement(self) -> None:
        """Exibe as operações e balanço da conta."""
        for item in self.__operations:
            print(item)
        print(f"Balance: {self.__balance}")

    def __validate_positive_amount(self, amount: int) -> None:
        """Valida se o valor (amount) é maior que zero.
        Args:
            amount: O valor a ser verificado.
        Raises:
            ValueError: Se o valor for menor ou igual a zero.
        """
        if amount <= 0:
            raise ValueError("O valor deve ser > 0")

    def __update_balance(self, value: int) -> None:
        """Atualiza balanço.
        Args:
            value: O valor a adicionado ou subtraido do balanço.
        """
        self.__balance += value

    def __update_operations(self, operation: str) -> None:
        """Atualiza historico de ooperações.
        Args:
            operation: A operação a ser adicionada no historico.
        """
        self.__operations.append(operation)


ac = Account(123, "123.456.789-01")
# >>> ac
# Account(123, '123.456.789-01')
# >>> print(ac)
# Account: 123
# Balance: [+] R$ 0,00
ac.deposit(1122200, "ATM deposit")
ac.withdraw(1000000, "ATM withdraw")
ac.statement()
# [+] R$ 11.222,00 (ATM deposit)
# Balance: [+] R$ 11.222,00
