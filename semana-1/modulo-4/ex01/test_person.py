import pytest
from person import Person


test_data_p = [
    pytest.param("Alice", 30, id="test_p1"),
    pytest.param("Bruno", 18, id="test_p2"),
    pytest.param("Carla", 14, id="test_p3"),
]


@pytest.mark.parametrize("intput, output", test_data_p)
def test_create_person(intput: str, output: int) -> None:
    p = Person(intput, output)
    assert p.name == intput
    assert p.age == output


test_data_b = [
    pytest.param("Alice", 30, 31, id="test_b1"),
    pytest.param("Bruno", 18, 19, id="test_b2"),
    pytest.param("Carla", 14, 15, id="test_b3"),
]


@pytest.mark.parametrize("nome, idade, output", test_data_b)
def test_birthday(nome: str, idade: int, output: int) -> None:
    p = Person(nome, idade)
    expected = output
    p.birthday()
    result = p.age
    assert expected == result
