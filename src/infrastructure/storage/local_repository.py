
import os
from typing import List
from ...entities.interfaces import GCodeRepository

class FileGCodeRepository(GCodeRepository):
    """Implementación de persistencia en sistema de archivos local."""
    def __init__(self, base_path: str = "data"):
        self._base_path = base_path
        os.makedirs(self._base_path, exist_ok=True)

    def save(self, gcode_lines: List[str], filename: str) -> str:
        ruta_completa = os.path.join(self._base_path, filename)
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write("\n".join(gcode_lines))
        return os.path.abspath(ruta_completa)
