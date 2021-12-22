"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
