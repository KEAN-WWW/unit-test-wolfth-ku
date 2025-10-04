from tests.Calculator import sub


def test_subtraction():
    assert sub(2,1) == 1
    assert sub(2,-3) == 5
    assert sub(-3,2) == -5
    assert sub (-3,-3) ==0
    assert sub(3,0) == 3
    pass