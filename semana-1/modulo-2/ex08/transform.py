import sys


def square_even_numbers(list_inteiros: list[int]) -> list[int]:
    """
    A função recebe uma lista de inteiros
    retorna uma nova lista contendo o quadrado apenas dos números pares
    """
    return [x**2 for x in list_inteiros if x % 2 == 0]


if __name__ == "__main__":
    tamanho_entrada = len(sys.argv)
    if tamanho_entrada > 1:
        str_values = sys.argv[1]
        list_int_values = list(map(int, str_values.split(" ")))
        print(square_even_numbers(list_inteiros=list_int_values))
    else:
        print(None)
