"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    fib_1, fib_2 = 1, 1
    yield fib_1
    yield fib_2
    while True:
        fib_2, fib_1 = fib_1 + fib_2, fib_2
        yield fib_2


fibonacci_gen = fibonacci()
