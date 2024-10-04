from supermath.arithmetique import addition, soustraction


def test_addition():
    assert addition(10, 3) == 13


def test_soustraction():
    assert soustraction(10, 3) == 7
