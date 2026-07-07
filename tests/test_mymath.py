import pytest

from mymath import add, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 1


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="除数不能为 0"):
        divide(-10, 0)
