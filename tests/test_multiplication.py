"""
tests multiplication
"""
from Calculator import mul

def test_multiplication():
    """Tests Multiplication"""
    assert mul(2,2) == 4
    assert mul(2,-2) == -4
    assert mul(-2,-2) == 4
