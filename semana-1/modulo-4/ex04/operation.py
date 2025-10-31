from utils import format_cents


class Operation:
    """Representa uma transação financeira."""

    def __init__(self, cents: int, description: str):
        """Inicializa um novo objeto Operação.

        Args:
            cents (int): O nome da pessoa.
            operation_type (str): A idade da pessoa.
            description (str): A idade da pessoa.
        """
        self.cents = cents
        self.description = description
        self.operation_type = self.__determine_operation_type()
        if cents == 0:
            raise ValueError("O valor de cents deve ser diferente de zero")

    def __repr__(self) -> str:
        """Retorna a representação oficial do objeto,seguindo o formato:
        Operation(cents=..., operation_type=..., description=...)
        """
        return (
            f"Operation(cents={self.cents}, "
            f"operation_type='{self.operation_type}', "
            f"description='{self.description}')"
        )

    def __str__(self) -> str:
        """Retorna uma string amigável para o usuário quando o objeto é impresso."""
        return f"[{'-' if self.operation_type == 'debit' else '+'}] {format_cents(abs(self.cents))} ({self.description})"

    def __determine_operation_type(self) -> str:
        """Retorna o valor para operation_type seguindo as regras:
        Se cents > 0, então operation_type = ’credit’
        Se cents < 0, então operation_type = ’debit’
        """
        if self.cents > 0:
            return "credit"
        elif self.cents < 0:
            return "debit"
        else:
            return ""
