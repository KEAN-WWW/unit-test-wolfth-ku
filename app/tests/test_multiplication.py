from tests.Calculator import mul


def test_multiplication():
    assert mul(2,2) == 4
    assert mul(2,-2) == -4
    assert mul(-2,-2) == 4
    pass