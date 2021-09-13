from tasks.easy.decorators.logging_decorator import log_decorator, hello


def test_hello(capsys):
    hello("Slava")
    captured = capsys.readouterr()
    assert captured.out == "Выполняем hello с args: ('Slava',) и kwargs: {}\nПривет, Slava\nВыполнено hello\n"


def test_log_decorator(capsys):
    def function(a, *, b):
        pass

    func_with_decorator = log_decorator(function)
    func_with_decorator(1, b=2)

    captured = capsys.readouterr()
    assert captured.out == "Выполняем function с args: (1,) и kwargs: {'b': 2}\nВыполнено function\n"
