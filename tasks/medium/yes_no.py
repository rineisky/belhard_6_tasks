"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1: list) -> str:
    list_of_unique = []
    unique_n = set(list_1)
    for i in unique_n:
        list_of_unique.append(i)
    t = "No"
    if len(list_1) > len(list_of_unique):
        t = "Yes"
    return t


print(yes_or_no([1, 2, 3, 3, 4]))

