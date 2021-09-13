import pytest

from tasks.medium.fibonacci_generator import fibonacci


def test_fibonacci():
    with pytest.raises(ValueError):
        generator = fibonacci(0)
        next(generator)

    generator = fibonacci(5)
    assert next(generator) == 1
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 5

    with pytest.raises(StopIteration):
        next(generator)
