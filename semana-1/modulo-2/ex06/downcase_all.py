import sys


def downcase_it(value: str) -> str:
    """
    A função recebe um valor string e transforma a string em low case
    returm string low case
    """
    return value.lower()


if __name__ == "__main__":
    tamanho_entrada = len(sys.argv)
    if tamanho_entrada > 1:
        for i in range(1, tamanho_entrada):
            print(downcase_it(sys.argv[i]))
    else:
        print(None)
