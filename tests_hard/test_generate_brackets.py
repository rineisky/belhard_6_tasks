import pytest

from tasks.hard.generate_brackets import generate_brackets


@pytest.mark.parametrize(
    "n, expected", (
        (3, """((()))
(()())
(())()
()(())
()()()"""),
        (4, """(((())))
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
()()()()""")
    )
)
def test_generate_brackets(capsys, n, expected):
    generate_brackets(n)
    assert capsys.readouterr().out == expected + "\n"
