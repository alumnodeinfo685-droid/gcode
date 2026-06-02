
from typing import List

class Point:
    """Value Object que representa una coordenada bidimensional."""
    def __init__(self, x: float, y: float):
        self._x = round(x, 4)
        self._y = round(y, 4)

    @property
    def x(self) -> float: return self._x

    @property
    def y(self) -> float: return self._y


class Path:
    """Entidad que representa un trazo continuo (un polígono abierto o cerrado)."""
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


class TextGeometry:
    """Agregado (Aggregate Root) que contiene el conjunto de trazos de un texto."""
    def __init__(self, text: str, paths: List[Path]):
        self._text = text
        self._paths = paths

    @property
    def text(self) -> str: return self._text

    @property
    def paths(self) -> List[Path]: return self._paths


class MachineConfig:
    """Value Object con los parámetros tecnológicos de la máquina CNC."""
    def __init__(self, safe_z: float, work_z: float, feed_rate_xy: float, feed_rate_z: float):
        self.safe_z = safe_z          # Altura de seguridad (Z arriba)
        self.work_z = work_z          # Profundidad de grabado (Z abajo)
        self.feed_rate_xy = feed_rate_xy  # Velocidad de avance X-Y
        self.feed_rate_z = feed_rate_z    # Velocidad de penetración Z
