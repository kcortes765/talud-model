"""Cálculos principales de estabilidad de taludes."""

from __future__ import annotations

from math import sin, cos
from typing import List

import numpy as np

from src.data.models import CirculoFalla, Dovela, Estrato, PerfilTerreno


def crear_dovelas(circulo: CirculoFalla, n: int) -> List[Dovela]:
    """Divide el círculo de falla en ``n`` dovelas."""
    angulos = np.linspace(0, 2 * np.pi, n, endpoint=False)
    dovelas = []
    for ang in angulos:
        peso = 1.0  # valor ficticio para peso
        presion = 0.0  # sin presión de poros inicial
        y_base = circulo.y_centro - circulo.radio * sin(ang)
        y_superficie = circulo.y_centro + circulo.radio * sin(ang)
        dovelas.append(Dovela(angulo=ang, peso=peso, presion_porop=presion,
                              y_base=y_base, y_superficie=y_superficie))
    return dovelas


def bishop_simplificado(dovelas: List[Dovela], angulo_inclinacion: float) -> float:
    """Calcula el factor de seguridad con el método de Bishop simplificado."""
    resistencia = sum(d.peso * cos(d.angulo) for d in dovelas)
    esfuerzo = sum(d.peso * sin(d.angulo + angulo_inclinacion) for d in dovelas)
    if esfuerzo == 0:
        raise ZeroDivisionError("Esfuerzo nulo en Bishop")
    return abs(resistencia / esfuerzo)


def fellenius(dovelas: List[Dovela], angulo_inclinacion: float) -> float:
    """Calcula el factor de seguridad con el método de Fellenius."""
    resistencia = sum(d.peso * cos(d.angulo) for d in dovelas)
    esfuerzo = sum(d.peso * sin(d.angulo + angulo_inclinacion) for d in dovelas)
    if esfuerzo == 0:
        raise ZeroDivisionError("Esfuerzo nulo en Fellenius")
    return abs(resistencia / esfuerzo)
