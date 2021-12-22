"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, c=1, s=""):
    if c <= n:
        return triangular_sequence(n, c + 1, s + str(c) * c + "\n")
    else:
        return s
