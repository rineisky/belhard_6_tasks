def dict_from_args(*args, **kwargs):
    if all(isinstance(key, int) for key in args):
        sum1 = {"args_sum": sum(args)}
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if all(isinstance(values, str) for values in kwargs):
        max_len = {
            "kwargs_max_len":
                max(len(values) for values in kwargs.values())
        }
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    sum1.update(max_len)
    return sum1


if __name__ == '__main__':
    dict_from_args(*(41, 50, 13), **{"1": "jhbv", "2": "khgckhgc"})
