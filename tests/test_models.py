from src.data import models


def test_circulo_falla():
    c = models.CirculoFalla(1.0, 2.0, 3.0)
    assert c.x_centro == 1.0
    assert c.y_centro == 2.0
    assert c.radio == 3.0


def test_dovela_attributes():
    d = models.Dovela(angulo=0.0, peso=1.0, presion_porop=0.0, y_base=0.0, y_superficie=1.0)
    assert d.y_base == 0.0
    assert d.y_superficie == 1.0
