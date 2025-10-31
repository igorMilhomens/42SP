import pytest
from utils import format_cents


test_data = [
    pytest.param(11_222_00, "R$ 11.222,00", id="test_1"),
    pytest.param(222_00, "R$ 222,00", id="test_2"),
    pytest.param(2_00, "R$ 2,00", id="test_3"),
]


@pytest.mark.parametrize("input, output", test_data)
def test_sucess(input: int, output: str) -> None:
    given = input
    expected = output
    result = format_cents(given)
    assert result == expected
