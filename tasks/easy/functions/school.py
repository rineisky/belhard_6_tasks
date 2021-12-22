"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(some_dict: dict, n_classes: str):
    some_dict[n_classes] += 1
    return some_dict


def decr_students(some_dict: dict, n_classes: str):
    if some_dict[n_classes] > 0:
        some_dict[n_classes] -= 1
    else:
        return some_dict
    return some_dict


def add_class(some_dict: dict, n_classes: str):
    some_dict[n_classes] = 0
    return some_dict


def remove_class(some_dict: dict, n_classes: str):
    some_dict.pop(n_classes)
    return some_dict


def calc_students(some_dict: dict):
    quant_st = sum(some_dict.values())
    return quant_st
