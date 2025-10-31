import sys


def is_positive(valor: int) -> int:
    """
    A função recebe um valor inteiro
    return: Retorna um booleand (False/True) indicando se o valor é inteiro
    """
    return valor > 0


if __name__ == "__main__":
    print(is_positive(int(sys.argv[1])))
