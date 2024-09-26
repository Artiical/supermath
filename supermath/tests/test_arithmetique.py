def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a / b


def division_entiere(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a // b


def modulo(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a % b


def exposant(a, b):
    return a**b


def test_addition():
    assert addition(10, 4) == 13


def test_soustraction():
    assert soustraction(10, 1) == 7
