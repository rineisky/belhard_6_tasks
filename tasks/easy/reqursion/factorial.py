"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n, current=1, result=1):
    if current <= n:
        return factorial(n, current + 1, result * current)
    else:
        return result
