from src.core.calculos import crear_dovelas, bishop_simplificado, fellenius
from src.data.models import CirculoFalla


def test_crear_dovelas_numero():
    c = CirculoFalla(0.0, 0.0, 1.0)
    dovelas = crear_dovelas(c, 4, 18.0)
    assert len(dovelas) == 4


def test_bishop_and_fellenius():
    c = CirculoFalla(0.0, 0.0, 1.0)
    dovelas = crear_dovelas(c, 4, 18.0)
    fs_b = bishop_simplificado(dovelas, 30.0)
    fs_f = fellenius(dovelas, 30.0)
    assert fs_b > 0
    assert fs_f > 0
