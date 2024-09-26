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


# Variables
a = 10
b = 3

# Calculs
resultat_addition = addition(a, b)
resultat_soustraction = soustraction(a, b)
resultat_multiplication = multiplication(a, b)
resultat_division = division(a, b)
resultat_division_entiere = division_entiere(a, b)
resultat_modulo = modulo(a, b)
resultat_exposant = exposant(a, b)

# Affichage des résultats
print("Addition:", resultat_addition)
print("Soustraction:", resultat_soustraction)
print("Multiplication:", resultat_multiplication)
print("Division:", resultat_division)
print("Division entière:", resultat_division_entiere)
print("Modulo:", resultat_modulo)
print("Exposant:", resultat_exposant)
