"""Cálculos principales de estabilidad de taludes."""

from __future__ import annotations

from math import sin, cos, tan
from typing import List

import numpy as np

from src.data.models import CirculoFalla, Dovela, Estrato, PerfilTerreno


def crear_dovelas(circulo: CirculoFalla, n: int, peso_unitario: float) -> List[Dovela]:
    """Divide el círculo de falla en ``n`` dovelas y calcula su peso."""
    angulos = np.linspace(0, 2 * np.pi, n, endpoint=False)
    delta = 2 * np.pi / n
    dovelas: List[Dovela] = []
    for ang in angulos:
        area = 0.5 * circulo.radio ** 2 * delta
        peso = area * peso_unitario
        presion = 0.0  # sin presión de poros inicial
        y_base = circulo.y_centro - circulo.radio * sin(ang)
        y_superficie = circulo.y_centro + circulo.radio * sin(ang)
        dovelas.append(
            Dovela(
                angulo=ang,
                peso=peso,
                presion_porop=presion,
                y_base=y_base,
                y_superficie=y_superficie,
            )
        )
    return dovelas


def bishop_simplificado(dovelas: List[Dovela], angulo_friccion: float) -> float:
    """Calcula el factor de seguridad con el método de Bishop simplificado."""
    phi = np.deg2rad(angulo_friccion)
    esfuerzo = sum(d.peso * sin(d.angulo) for d in dovelas)
    if esfuerzo == 0:
        raise ZeroDivisionError("Esfuerzo nulo en Bishop")
    resistencia = sum(d.peso * tan(phi) for d in dovelas)
    return abs(resistencia / esfuerzo)


def fellenius(dovelas: List[Dovela], angulo_friccion: float) -> float:
    """Calcula el factor de seguridad con el método de Fellenius."""
    phi = np.deg2rad(angulo_friccion)
    denominador = sum(d.peso * sin(d.angulo) for d in dovelas)
    if denominador == 0:
        raise ZeroDivisionError("Esfuerzo nulo en Fellenius")
    numerador = sum(d.peso * tan(phi) * cos(d.angulo) for d in dovelas)
    return abs(numerador / denominador)
