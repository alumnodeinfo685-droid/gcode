
from abc import ABC, abstractmethod
from typing import List
from .models import TextGeometry, MachineConfig

class FontService(ABC):
    """Puerto (Abstracción) para el servicio de tipografía."""
    @abstractmethod
    def get_geometry(self, text: str, size: float) -> TextGeometry:
        pass


class GCodeFormatter(ABC):
    """Puerto para la transformación de trayectorias a dialectos G-code."""
    @abstractmethod
    def generate_gcode(self, geometry: TextGeometry, config: MachineConfig) -> List[str]:
        pass
