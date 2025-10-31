import pytest
import calculator


def test_add() -> None:
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract() -> None:
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5


def test_multiply() -> None:
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10


def test_divide() -> None:
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)


def test_power() -> None:
    assert calculator.power(10, 2) == 100
    assert calculator.power(2, -1) == 0.5


def test_power_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Zero cannot be raised to a negative power"):
        calculator.power(0, -2)
