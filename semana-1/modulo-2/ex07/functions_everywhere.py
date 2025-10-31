import sys


def shrink(value: str) -> str:
    """
    A função recebe um valor string com tamanho maior que 8
    return substring com os 8 primeiros caracteres
    """
    return value[:8]


def enlarge(value: str) -> str:
    """
    A função recebe um valor string com tamanho menor que 8 e completa string com 'Z' ao final até 8 caracteres
    return nova string com 8 carcteres
    """
    return value.ljust(8, "Z")


if __name__ == "__main__":
    tamanho_entrada = len(sys.argv)
    if tamanho_entrada > 1:
        for i in range(1, tamanho_entrada):
            item = sys.argv[i]
            tamanho_item = len(item)
            if tamanho_item < 8:
                print(enlarge(item))
            elif tamanho_item == 8:
                print(item)
            else:
                print(shrink(item))
    else:
        print(None)
