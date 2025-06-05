"""Dataclasses for slope stability models."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CirculoFalla:
    """Representa un círculo de falla potencial."""

    x_centro: float
    y_centro: float
    radio: float


@dataclass
class Estrato:
    """Propiedades de un estrato del talud."""

    angulo_interno: float
    cohesion: float
    peso_unitario: float


@dataclass
class Dovela:
    """Segmento de material empleado en los cálculos."""

    angulo: float
    peso: float
    presion_porop: float
    y_base: float
    y_superficie: float


@dataclass
class PerfilTerreno:
    """Conjunto de puntos que definen el perfil del terreno."""

    xs: List[float]
    ys: List[float]


@dataclass
class PropiedadesSuelo:
    """Propiedades globales del suelo."""

    peso_unitario: float
    angulo_friccion: float
    cohesion: float
    porosidad: Optional[float] = None
