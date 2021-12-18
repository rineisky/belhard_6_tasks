"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n, counter=1, summa=0) -> int:
    if counter <= len(str(n)):
        return sum_of_numbers(n, counter + 1, summa + get_number(n, counter))
    else:
        return summa


def get_number(n, counter):
    return int(list(str(n))[counter - 1])
