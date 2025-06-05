from src.core.optimizacion import smart_circle_optimizer


def test_optimizer_returns_result():
    res = smart_circle_optimizer([0, 1, 0, 1, 0.5, 1.0], n_dovelas=3)
    assert res.factor_seguridad > 0
    assert res.circulo.radio >= 0.1
