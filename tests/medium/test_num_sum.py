import pytest

from tasks.medium.num_sum import sum_of_numbers


@pytest.mark.parametrize(
    "n, expected", (
        (123, 6),
        (1111111, 7),
        (4, 4),
        (935145, 27),
    )
)
def test_sum_of_numbers(n, expected):
    assert sum_of_numbers(n) == expected
