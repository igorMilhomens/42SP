def average(values_dict: dict[str, int]) -> float:
    """
    Receba um dicionário com nomes e notas
    Retorna a média da turma
    """
    if values_dict:
        soma = sum(values_dict.values())
        quantidade = len(values_dict)
        return soma / quantidade
    else:
        return 0
