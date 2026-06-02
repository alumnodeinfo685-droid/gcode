
from abc import ABC, abstractmethod
from typing import List
from .models import TextGeometry, MachineConfig

class FontService(ABC):
    """Puerto para el servicio de tipografía."""
    @abstractmethod
    def get_geometry(self, text: str, size: float) -> TextGeometry:
        pass


class GCodeFormatter(ABC):
    """Puerto para la transformación de trayectorias a dialectos G-code."""
    @abstractmethod
    def generate_gcode(self, geometry: TextGeometry, config: MachineConfig) -> List[str]:
        pass


class GCodeRepository(ABC):
    """Puerto para el almacenamiento de archivos G-code (Persistencia)."""
    @abstractmethod
    def save(self, gcode_lines: List[str], filename: str) -> str:
        """Guarda las líneas y retorna la ruta completa del archivo."""
        pass
