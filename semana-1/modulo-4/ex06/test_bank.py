from bank import Bank
from account import Account


def test_import_bank_success() -> None:
    given = Bank()
    expected = Bank
    assert isinstance(given, expected)


def test_add_account() -> None:
    given = Bank()
    given.add_account(Account(123, "123.456.789-01"))
    expected = 1
    result = len(given)
    assert result == expected


def test_get_account_by_cpf() -> None:
    given = Bank()
    given.add_account(Account(123, "123.456.789-01"))
    expected = Account(123, "123.456.789-01")
    result = given.get_account_by_cpf("123.456.789-01")
    assert result.account_id == expected.account_id
    assert result.cpf == expected.cpf


def test_get_account_by_id() -> None:
    given = Bank()
    given.add_account(Account(123, "123.456.789-01"))
    expected = Account(123, "123.456.789-01")
    result = given.get_account_by_id(123)
    assert result.account_id == expected.account_id
    assert result.cpf == expected.cpf


def test_transfer() -> None:
    bank = Bank()
    ac1 = Account(123, "123.456.789-01")
    ac2 = Account(456, "234.567.890-12")
    bank.add_account(ac1)
    bank.add_account(ac2)
    bank[123].deposit(10000, "Initial deposit")
    valor_transferencia = 5000
    bank.transfer(123, 456, valor_transferencia, "Payment")

    assert ac1.get_balance() == 10000 - valor_transferencia
    assert ac2.get_balance() == valor_transferencia
