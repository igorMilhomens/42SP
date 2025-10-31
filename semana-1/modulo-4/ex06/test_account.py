import pytest
from account import Account


def test_create_account_success() -> None:
    given = Account(123, "123.456.789-01")
    expected = "Account: 123\nBalance: [+] R$ 0,00"
    result = str(given)
    assert result == expected


test_data_deposit = [
    pytest.param(
        11_222_00, "[+] R$ 11.222,00 (ATM deposit)\nBalance: 1122200\n", id="test_1"
    ),
    pytest.param(200, "[+] R$ 2,00 (ATM deposit)\nBalance: 200\n", id="test_2"),
]


@pytest.mark.parametrize("amount, output", test_data_deposit)
def test_operations_deposit_success(
    amount: int, output: str, capsys: pytest.CaptureFixture[str]
) -> None:
    given = Account(123, "123.456.789-01")
    given.deposit(amount, "ATM deposit")
    given.statement()
    captured = capsys.readouterr()
    expected = output
    assert expected == captured.out


test_data_withdraw = [
    pytest.param(
        11_222_00,
        "[+] R$ 11.222,00 (ATM deposit)\n[-] R$ 11.222,00 (ATM withdraw)\nBalance: 0\n",
        id="test_1",
    ),
    pytest.param(
        200,
        "[+] R$ 2,00 (ATM deposit)\n[-] R$ 2,00 (ATM withdraw)\nBalance: 0\n",
        id="test_2",
    ),
]


@pytest.mark.parametrize("amount,output", test_data_withdraw)
def test_operations_withdraw_success(
    amount: int, output: str, capsys: pytest.CaptureFixture[str]
) -> None:
    given = Account(123, "123.456.789-01")
    given.deposit(amount, "ATM deposit")
    given.withdraw(amount, "ATM withdraw")
    given.statement()
    captured = capsys.readouterr()
    expected = output
    assert expected == captured.out
