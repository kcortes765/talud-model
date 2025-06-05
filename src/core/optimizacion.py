"""Algoritmos de optimización para encontrar el círculo de falla crítico."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np

from src.core.calculos import bishop_simplificado, crear_dovelas
from src.data.models import CirculoFalla


@dataclass
class OptimizacionResultado:
    circulo: CirculoFalla
    factor_seguridad: float


def validar_y_corregir_circulo(circulo: CirculoFalla) -> CirculoFalla:
    """Ajusta el círculo en caso de que los parámetros sean no físicos."""
    radio = max(circulo.radio, 0.1)
    return CirculoFalla(circulo.x_centro, circulo.y_centro, radio)


def smart_circle_optimizer(rangos: List[float], n_dovelas: int) -> OptimizacionResultado:
    """Búsqueda simple del círculo crítico dentro de los rangos dados.

    ``rangos`` es [xmin, xmax, ymin, ymax, rmin, rmax].
    """
    xmin, xmax, ymin, ymax, rmin, rmax = rangos
    mejor_fs = float("inf")
    mejor_circulo = None
    for x in np.linspace(xmin, xmax, 5):
        for y in np.linspace(ymin, ymax, 5):
            for r in np.linspace(rmin, rmax, 5):
                circulo = validar_y_corregir_circulo(CirculoFalla(x, y, r))
                dovelas = crear_dovelas(circulo, n_dovelas)
                fs = bishop_simplificado(dovelas, 0.0)
                if fs < mejor_fs:
                    mejor_fs = fs
                    mejor_circulo = circulo
    if mejor_circulo is None:
        raise ValueError("No se encontró un círculo válido")
    return OptimizacionResultado(circulo=mejor_circulo, factor_seguridad=mejor_fs)
