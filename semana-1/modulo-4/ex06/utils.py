def format_cents(value: int) -> str:
    """Formata um numero inteiro em uma string indicando um valor em real
    Ex. 11_222_00 que é em inteiro 1122200 é formatado para a string "R$ 11.222,00"
    """
    value_float = value / 100
    value_str_us = f"{value_float:,.2f}"
    value_str = value_str_us.replace(",", "#").replace(".", ",").replace("#", ".")
    return f"R$ {value_str}"
