from typing import Any, Optional


def add(a: int, b: int) -> int:
    """
    A função soma dois numeros inteiros
    Retorna a soma
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    A função subtrai dois numeros inteiros
    Retorna a subtração
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    A função multiplica dois numeros inteiros
    Retorna a multiplicação
    """
    return a * b


def divide(a: int, b: int) -> Optional[float]:
    """
    A função divide dois numeros inteiros
    Retorna a divisão
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def power(base: int, exponent: int) -> Any:
    """
    A função calcula exponeciação de dois numeros inteiros
    Retorna a exponenciação
    """
    try:
        return base**exponent
    except ZeroDivisionError:
        raise ValueError("Zero cannot be raised to a negative power")
