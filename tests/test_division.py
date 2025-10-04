import pytest

from tests.Calculator import div


def test_division():
    assert div(22,2) == 11
    assert div(2,-2) == -1
    assert div(-2,-2) == 1
    pass

def test_divide_zero_exception():
    assert div(2,0)
    with pytest.raises(ZeroDivisionError):
        pass