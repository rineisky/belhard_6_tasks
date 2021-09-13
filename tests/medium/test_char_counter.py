from tasks.medium.char_counter import count_char


def test_count_char():
    assert count_char("best test ever") == {
        "b": 1,
        "e": 4,
        "s": 2,
        "t": 3,
        " ": 2,
        "v": 1,
        "r": 1
    }
