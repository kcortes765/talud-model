"""Validación de datos de entrada para los cálculos."""

from __future__ import annotations

from dataclasses import dataclass


class DatosInvalidosError(ValueError):
    """Excepción para datos inválidos."""


@dataclass
class Rango:
    minimo: float
    maximo: float

    def contiene(self, valor: float) -> bool:
        return self.minimo <= valor <= self.maximo


def validar_valor(valor: float, rango: Rango, nombre: str) -> None:
    if not rango.contiene(valor):
        raise DatosInvalidosError(f"{nombre} fuera de rango")
