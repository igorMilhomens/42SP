import pytest
from pydantic import ValidationError

from validate import Account


def test_validate_with_failure() -> None:
    account = {"name": "Fulano", "age": None, "email": "fulano@email", "balance": 0.0}
    with pytest.raises(ValidationError):
        Account.model_validate(account)


def test_validate_with_success() -> None:
    account = {"name": "Fulano", "age": 1, "email": "fulano@email", "balance": 0.0}

    assert Account.model_validate(account)


def test_validate_with_wrong_types() -> None:
    account = {"name": "15", "age": "idate", "email": "fulano@email", "balance": "0.0"}

    with pytest.raises(ValidationError, match="1 validation error for Account\nage\n"):
        Account.model_validate(account)
