"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n: int):
    if n <= 0:
        return 1
    if n > 0:
        return n * factorial(n - 1)


print(factorial(5))
