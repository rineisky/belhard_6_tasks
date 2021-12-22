"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
some_list = [1, 5, 7, 9, 10, 1, 2, 7, 5]


def yes_or_no(some):
    met = set()
    for i in some:
        if i not in met:
            met.add(i)
            print("No")
        else:
            print("Yes")
