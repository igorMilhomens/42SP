import sys


def metodos_string(valor: str) -> None:
    """
    A função recebe um valor string e apreenta os metodos ja implementados de string no python
    """
    print(f"São maíusculas? {valor.isupper()}")
    print(f"É númerico? {valor.isnumeric()}")
    print(f"É ascii?  {valor.isascii()}")
    print(f"É alfanumérico? {valor.isalnum()}")


if __name__ == "__main__":
    metodos_string(sys.argv[1])
