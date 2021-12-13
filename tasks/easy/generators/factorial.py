"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

b = True


def factorial():
    pr = 1
    val = 1
    while b:
        pr *= val
        val += 1
        yield pr


factorial_gen = factorial()
print(next(factorial_gen))
print(next(factorial_gen))
