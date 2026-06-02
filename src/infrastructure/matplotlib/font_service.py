
from typing import List
from matplotlib.textpath import TextPath
from ...entities.models import Point, Path, TextGeometry
from ...entities.interfaces import FontService

class MatplotlibFontService(FontService):
    """Implementación del FontService utilizando Matplotlib para vectorizar texto."""
    def get_geometry(self, text: str, size: float) -> TextGeometry:
        # Crea un path vectorial usando las fuentes del sistema/matplotlib
        matplotlib_path = TextPath((0, 0), text, size=size)
        
        # 'to_polygons' simplifica el path (incluyendo curvas de Bézier) a segmentos lineales
        # Esto soluciona el problema de letras como la 'O' que se definen mayormente por curvas
        polygons = matplotlib_path.to_polygons()

        paths: List[Path] = []
        for poly in polygons:
            current_path = Path()
            for vertex in poly:
                current_path.add_point(Point(vertex[0], vertex[1]))
            
            if not current_path.is_empty:
                paths.append(current_path)

        return TextGeometry(text, paths)
