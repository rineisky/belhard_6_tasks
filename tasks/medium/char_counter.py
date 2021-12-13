"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
import pprint

STR_VAL = 'python is the fastest-growing major programming language'


def count_char(text: str) -> dict:
    quantity = {}
    for i in text:
        quantity.setdefault(i, 0)
        quantity[i] += 1

    return quantity


pprint.pprint(count_char(STR_VAL))
