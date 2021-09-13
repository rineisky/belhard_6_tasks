import pytest

from tasks.easy.functions.add_number import add_numb


@pytest.mark.parametrize(
    "a, b, expected", (
        (2, 3, 5),
        (3, 7, 10)
    )
)
def test_add_number(a, b, expected):
    inner = add_numb(a)
    assert inner(b) == expected