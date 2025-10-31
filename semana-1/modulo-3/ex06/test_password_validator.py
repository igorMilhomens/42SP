import pytest
from password_validator import (
    is_valid_password,
    validate_char_upper,
    validate_char_lower,
    validate_char_num,
    validate_char_spec,
    validate_space,
)


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO*silva!2025", True),
        ("joao *silva!2025", False),
        ("JOAO*SILVA!2025", False),
        ("JOAO*silva!", False),
        ("JOAOsilva2025", False),
        ("JOAO *silva!2025", False),
        ("JOAO*silva!2025LARGE", False),
        ("2Small@", False),
    ],
    ids=[
        "test_success_password",
        "test_fail_validate_char_upper",
        "test_fail_validate_char_lower",
        "test_fail_validate_char_num",
        "test_fail_validate_char_spec",
        "test_fail_validate_space",
        "test_fail_password_large",
        "test_fail_password_small",
    ],
)
def test_is_valid_password(input: str, output: bool) -> None:
    given = input
    expected = output
    result = is_valid_password(given)
    assert result == expected


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO", True),
        ("joao", False),
    ],
    ids=["test_success_upper", "test_fail_upper"],
)
def test_validate_char_upper(input: str, output: bool) -> None:
    given = input
    expected = output
    result = validate_char_upper(given)
    assert result == expected


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO", False),
        ("joao", True),
    ],
    ids=["test_success_lower", "test_fail_lower"],
)
def test_validate_char_lower(input: str, output: bool) -> None:
    given = input
    expected = output
    result = validate_char_lower(given)
    assert result == expected


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO2025", True),
        ("joao", False),
    ],
    ids=["test_success_upper", "test_fail_upper"],
)
def test_validate_char_num(input: str, output: bool) -> None:
    given = input
    expected = output
    result = validate_char_num(given)
    assert result == expected


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO*", True),
        ("joao", False),
    ],
    ids=["test_success_num", "test_fail_num"],
)
def test_validate_char_spec(input: str, output: bool) -> None:
    given = input
    expected = output
    result = validate_char_spec(given)
    assert result == expected


@pytest.mark.parametrize(
    "input, output",
    [
        ("JOAO", True),
        ("joao ", False),
    ],
    ids=["test_success_space", "test_fail_space"],
)
def test_validate_space(input: str, output: bool) -> None:
    given = input
    expected = output
    result = validate_space(given)
    assert result == expected
