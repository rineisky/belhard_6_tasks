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


def triangular_sequence(n: int, x=1):
    if x <= n:
        print(str(x) * x)
        triangular_sequence(n, x=x + 1)
        print


triangular_sequence(5)
