import pytest

from tasks.easy.reqursion.triangular_sequence import triangular_sequence


@pytest.mark.parametrize(
    "n, expected", (
        (1, "1\n"),
        (2, "1\n22\n"),
        (3, "1\n22\n333\n"),
    )
)
def test_triangular_sequence(n, expected):
    assert triangular_sequence(n) == expected
