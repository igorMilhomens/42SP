def format_names(values_dict: dict[str, str]) -> list[str]:
    """
    Recebe um dicionário com nomes e sobrenomes
    Retorne uma lista com os nomes completos
    """
    values_list = []
    for chave, valor in values_dict.items():
        values_list.append(f"{chave.capitalize()} {valor.capitalize()}")
    return values_list
