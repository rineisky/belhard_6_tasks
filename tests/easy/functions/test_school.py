import pytest

from tasks.easy.functions.school import (
    incr_students,
    decr_students,
    add_class,
    remove_class,
    calc_students,
)


@pytest.fixture
def school_data():
    return {
        "1a": 15,
        "1b": 10,
        "2a": 20,
        "2b": 30
    }


def test_incr_students(school_data):
    incr_students(school_data, "1a")
    assert school_data["1a"] == 16


def test_decr_students(school_data):
    decr_students(school_data, "1a")
    assert school_data["1a"] == 14


def test_add_class(school_data):
    add_class(school_data, "3b")
    assert school_data["3b"] == 0


def test_remove_class(school_data):
    remove_class(school_data, "1a")
    assert "1a" not in school_data


def test_calc_students(school_data):
    assert calc_students(school_data) == 75
