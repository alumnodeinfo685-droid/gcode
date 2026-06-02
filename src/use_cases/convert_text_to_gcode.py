
from typing import List
from ..entities.models import MachineConfig
from ..entities.interfaces import FontService, GCodeFormatter

class ConvertTextToGCodeUseCase:
    """Caso de Uso: Orquesta la conversión de un texto plano a bloques de G-code."""
    def __init__(self, font_service: FontService, gcode_formatter: GCodeFormatter):
        # Inyección de dependencias (DIP de SOLID)
        self._font_service = font_service
        self._gcode_formatter = gcode_formatter

    def execute(self, text: str, font_size: float, config: MachineConfig) -> List[str]:
        if not text:
            raise ValueError("El texto a convertir no puede estar vacío.")
        
        # 1. Obtener la geometría abstracta del texto a través del servicio
        geometry = self._font_service.get_geometry(text, font_size)
        
        # 2. Formatear la geometría al formato G-code requerido
        gcode_lines = self._gcode_formatter.generate_gcode(geometry, config)
        
        return gcode_lines
