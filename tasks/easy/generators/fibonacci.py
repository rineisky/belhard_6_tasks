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
    fib1, fib2 = 0, 1
    val = 1
    while True:
        sum_ = fib1 + fib2
        fib1 = fib2
        fib2 = sum_
        val += 1
        yield fib1


fibonacci_gen = fibonacci()
