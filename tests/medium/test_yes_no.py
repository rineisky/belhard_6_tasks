from tasks.medium.yes_no import yes_or_no


def test_yes_or_no(capsys):
    yes_or_no([1, 2, 3, 2, 5, 6, 1, 7])
    captured = capsys.readouterr()
    assert captured.out == """\
No
No
No
Yes
No
No
Yes
No
"""
