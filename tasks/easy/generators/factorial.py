"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    n, fact = 1, 1
    while True:
        yield fact
        fact, n = fact * (n + 1), n + 1


factorial_gen = factorial()
