from Calculator import add


def test_addition():
    assert add(1,1) == 2
    assert add(1,-1) == 0
    assert add(-1,-1) == -2
    pass