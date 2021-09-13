from tasks.easy.generators.even_numbers import get_even_number


def test_get_even_number():
    generator = get_even_number()
    assert next(generator) == 2
    assert next(generator) == 4
    assert next(generator) == 6
    assert next(generator) == 8
