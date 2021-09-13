import pytest

from tasks.medium.check_number import check_number


@pytest.mark.parametrize(
    "n, expected", (
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (8, True),
        (256, True),
    )
)
def test_check_number(n, expected):
    assert check_number(n) is expected
