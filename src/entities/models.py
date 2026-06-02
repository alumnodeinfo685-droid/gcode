
from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    """Value Object inmutable que representa una coordenada bidimensional."""
    x: float
    y: float

    def __post_init__(self):
        # Aseguramos la precisión en el momento de la creación
        object.__setattr__(self, 'x', round(self.x, 4))
        object.__setattr__(self, 'y', round(self.y, 4))


class Path:
    """Entidad que representa un trazo continuo."""
    def __init__(self):
        self._points: List[Point] = []

    def add_point(self, point: Point):
        self._points.append(point)

    @property
    def points(self) -> List[Point]:
        return self._points

    @property
    def is_empty(self) -> bool:
        return len(self._points) == 0


@dataclass(frozen=True)
class TextGeometry:
    """Agregado que contiene el conjunto de trazos de un texto."""
    text: str
    paths: List[Path]


@dataclass(frozen=True)
class MachineConfig:
    """Value Object con los parámetros tecnológicos de la máquina CNC."""
    safe_z: float          # Altura de seguridad
    work_z: float          # Profundidad de grabado
    feed_rate_xy: float    # Velocidad de avance X-Y
    feed_rate_z: float     # Velocidad de penetración Z
