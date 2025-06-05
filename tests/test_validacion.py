from src.core.validacion import Rango, validar_valor, DatosInvalidosError


def test_validar_valor_ok():
    validar_valor(5, Rango(0, 10), "x")


def test_validar_valor_error():
    try:
        validar_valor(15, Rango(0, 10), "x")
    except DatosInvalidosError:
        assert True
    else:
        assert False
