from tasks.easy.generators.triangular_numbers import triangular_numbers


def test_triangular_numbers():
    generator = triangular_numbers()
    assert next(generator) == 1
    assert next(generator) == 3
    assert next(generator) == 6
    assert next(generator) == 10
    assert next(generator) == 15
    assert next(generator) == 21
