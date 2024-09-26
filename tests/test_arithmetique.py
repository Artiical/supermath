from supermath.arithmetique import addition, soustraction


def test_addition():
    assert addition(10, 4) == 13


def test_soustraction():
    assert soustraction(10, 1) == 7
