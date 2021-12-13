"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_of_numbers(num, res)
