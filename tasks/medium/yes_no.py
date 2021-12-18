"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(numbers_list):
    number_set = set()
    for number in numbers_list:
        if number not in number_set:
            number_set.add(number)
            print("No")
        else:
            print("Yes")
