from tasks.medium.burger_king import beef, chicken


def test_beef(capsys):
    beef()
    assert capsys.readouterr().out == """\
</------------\\>
----- лук ------
*** помидоры ****
### говядина ###
<\\____________/>
"""


def test_chicken(capsys):
    chicken()
    assert capsys.readouterr().out == """\
</------------\\>
^^^^^ сыр ^^^^^^
~~~~ салат ~~~~~
|||| курица ||||
<\\____________/>
"""
