class Person:
    """Representa uma pessoa com nome e idade."""

    def __init__(self, name: str, age: int):
        """Inicializa um novo objeto Pessoa.

        Args:
            name (str): O nome da pessoa.
            age (int): A idade da pessoa.
        """
        self.name = name
        self.age = age

    def birthday(self) -> None:
        """
        Incrementa a idade da pessoa em um ano.

        Este método não retorna nenhum valor (`None`).
        """
        self.age += 1
