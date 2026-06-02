
from typing import List
from ...entities.models import MachineConfig, TextGeometry
from ...entities.interfaces import GCodeFormatter

class StandardGCodeFormatter(GCodeFormatter):
    """Implementación de formateador G-code estándar (ISO / Marlin / Grbl)."""
    def generate_gcode(self, geometry: TextGeometry, config: MachineConfig) -> List[str]:
        gcode = []
        
        # Encabezado (Header) de Inicialización estándar
        gcode.append("; --- INICIO DEL ARCHIVO G-CODE ---")
        gcode.append(f"; Texto original: {geometry.text}")
        gcode.append("G21 ; Configurar unidades en milímetros (mm)")
        gcode.append("G90 ; Coordenadas absolutas")
        gcode.append(f"G0 Z{config.safe_z} ; Mover a altura segura inicial")
        gcode.append("M3 ; Enciender Husillo / Láser (Opcional)")
        gcode.append(";---")

        for i, path in enumerate(geometry.paths):
            if path.is_empty:
                continue
                
            gcode.append(f"; Iniciando trazo #{i + 1}")
            first_point = path.points[0]
            
            # 1. Movimiento rápido (Rápido - G0) al inicio del trazo (Z arriba)
            gcode.append(f"G0 X{first_point.x} Y{first_point.y}")
            
            # 2. Bajar herramienta controladamente (Avance - G1) a profundidad de trabajo
            gcode.append(f"G1 Z{config.work_z} F{config.feed_rate_z}")
            
            # 3. Maquinar/Dibujar el resto de los puntos del trazo
            for point in path.points[1:]:
                gcode.append(f"G1 X{point.x} Y{point.y} F{config.feed_rate_xy}")
            
            # 4. Retraer herramienta (Z arriba) antes de pasar al siguiente trazo
            gcode.append(f"G0 Z{config.safe_z}")
            gcode.append(";---")

        # Cierre del archivo (Footer)
        gcode.append("; --- FIN DEL ARCHIVO ---")
        gcode.append("M5 ; Apagar husillo")
        gcode.append("G0 X0 Y0 ; Retorno a HOME en X-Y")
        gcode.append("M30 ; Finalizar programa")
        
        return gcode
