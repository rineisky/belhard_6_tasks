"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n: int) -> bool:
    if n != 1 and n % 2 == 0:
        return check_number(n / 2)
    else:
        return False if n % 2 != 0 and n != 1 else True
