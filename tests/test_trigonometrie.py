from supermath.trigonometrie import calculer_cosinus, calculer_sinus, calculer_tangente

def test_cosinus(angle):
    assert calculer_cosinus(90) == 0

def test_sinus(angle):
    assert calculer_sinus(90) == 1

def test_tangente(angle):
    assert calculer_tangente(45) == 0