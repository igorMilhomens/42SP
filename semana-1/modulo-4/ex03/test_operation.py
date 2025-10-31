import pytest
from operation import Operation


test_data = [
    pytest.param(11_222_00, "ATM deposit", "credit", id="test_1"),
    pytest.param(-11_222_00, "ATM withdraw", "debit", id="test_2"),
]


@pytest.mark.parametrize("cents, description, outuput", test_data)
def test_success(cents: int, description: str, outuput: str) -> None:
    given = Operation(cents=cents, description=description)
    expected = outuput
    result = given.operation_type
    assert result == expected
