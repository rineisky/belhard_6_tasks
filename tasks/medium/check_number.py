"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1 or n == 2:
        return True
    if n % 2 != 0:
        return False
    n = int(n / 2.0)
    return check_number(n)


print(check_number(1))
