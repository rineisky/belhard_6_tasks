"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
some_list = [1, 2, 3, 4, 1, 5, 1, 7]


def yes_or_no(some: list) -> str:
    met = set()
    for i in some:
        if i in met:
            print("Yes")
        else:
            print("No")
            met.add(i)


yes_or_no(some_list)
