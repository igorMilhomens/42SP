from account import Account


class Bank:
    """
    Representa um sistema bancário que gerencia contas.

    A classe armazena uma lista de objetos do tipo Account e fornece métodos
    para adicionar, buscar e manipular essas contas, como realizar transferências.
    """

    def __init__(self) -> None:
        """
        Inicializa uma nova instância da classe Bank.

        Cria uma lista privada para armazenar as contas.
        """
        self.__accounts: list[Account] = []

    def __len__(self) -> int:
        """
        Retorna o número total de contas no banco.

        Retorna:
            int: O número de contas.
        """
        return len(self.__accounts)

    def __contains__(self, account: int) -> bool:
        """
        Verifica se uma conta com um determinado ID existe no banco.
        Args:
            account (int): O ID da conta a ser verificada.
        Retorna:
            bool: True se a conta existir, False caso contrário.
        """
        return any(item.account_id == account for item in self.__accounts)

    def __getitem__(self, account: int) -> Account:
        """
        Permite o acesso a uma conta pelo seu ID, como se fosse um dicionário.
        Args:
            account (int): O ID da conta.
        Retorna:
            Account: O objeto da conta correspondente.
        Raises:
            IndexError: Se a conta com o ID fornecido não existir.
        """
        list_account = [item for item in self.__accounts if item.account_id == account]
        if list_account:
            return list_account[0]
        else:
            raise IndexError(f"Conta: '{account}' inexistente")

    def add_account(self, account: Account) -> None:
        """
        Adiciona uma nova conta à lista de contas do banco.
        Args:
            account (Account): O objeto Account a ser adicionado.
        """
        self.__accounts.append(account)

    def get_account_by_cpf(self, cpf: str) -> Account:
        """
        Busca e retorna uma conta com base no CPF do titular.
        Args:
            cpf (str): O CPF do titular da conta.
        Retorna:
            Account: O objeto da conta correspondente.
        Raises:
            IndexError: Se nenhuma conta com o CPF fornecido for encontrada.
        """
        list_account = [item for item in self.__accounts if item.cpf == cpf]
        if list_account:
            return list_account[0]
        else:
            raise IndexError(f"CPF: '{cpf}' inexistente")

    def get_account_by_id(self, account_id: int) -> Account:
        """
        Busca e retorna uma conta com base no seu ID.
        Args:
            account_id (int): O ID da conta.
        Retorna:
            Account: O objeto da conta correspondente.
        Raises:
            IndexError: Se a conta com o ID fornecido não existir.
        """
        return self[account_id]

    def transfer(
        self,
        source_account: int,
        destination_account: int,
        value: int,
        description: str,
    ) -> None:
        """Account(123, "123.456.789-01")
        Realiza uma transferência de um valor entre duas contas.
        Args:
            source_account (int): O ID da conta de origem.
            destination_account (int): O ID da conta de destino.
            value (int): O valor a ser transferido.
            description (str): A descrição da transação.
        Raises:
            IndexError: Se a conta de origem ou destino não for encontrada.
        """
        account_source = self[source_account]
        account_destination = self[destination_account]
        account_source.withdraw(value, description)
        account_destination.deposit(value, description)
