import pytest

from tasks.easy.functions.arguments import dict_from_args


@pytest.mark.parametrize(
    "args, kwargs, expected", (
        ([1, 2], {"a": "aa", "b": "bbb"}, {"args_sum": 3, "kwargs_max_len": 3}),
        ([1, "2"], {"a": "aa", "b": "bbb"}, TypeError),
        ([1, 2], {"a": 2, "b": "bbb"}, TypeError),
    )
)
def test_dict_from_args(args, kwargs, expected):
    if expected is TypeError:
        with pytest.raises(TypeError):
            dict_from_args(*args, **kwargs)
    else:
        assert dict_from_args(*args, **kwargs) == expected
