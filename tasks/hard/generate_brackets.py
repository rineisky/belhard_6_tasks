"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_brackets(n, sequence="", opened=0, closed=0):
    if (n * 2) > len(sequence):
        if opened < n:
            generate_brackets(n, sequence + "(", opened + 1, closed)
        if opened > closed:
            generate_brackets(n, sequence + ")", opened, closed + 1)
    else:
        print(sequence)
