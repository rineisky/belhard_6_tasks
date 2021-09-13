from tasks.hard.line_print import line_print


def test_line_print(capsys):
    some_list = [1, [2], [1, [2], [5, 7], 3], 8]
    line_print(some_list)
    assert capsys.readouterr().out == """\
1
    2
    1
        2
        5
        7
    3
8
"""
