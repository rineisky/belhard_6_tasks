from tasks.easy.generators.factorial import factorial


def test_factorial():
    generator = factorial()
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 6
    assert next(generator) == 24
