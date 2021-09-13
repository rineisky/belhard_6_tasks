from tasks.easy.generators.fibonacci import fibonacci


def test_fibonacci():
    generator = fibonacci()
    assert next(generator) == 1
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 5
    assert next(generator) == 8

