"""
tests division
"""
import pytest

from Calculator import div

def test_division():
    """Tests Division functions"""

    assert div(22,2) == 11
    assert div(2,-2) == -1
    assert div(-2,-2) == 1

def test_divide_zero_exception():
    """Divides by Zero"""
    with pytest.raises(ZeroDivisionError):
        assert div(2, 0)
