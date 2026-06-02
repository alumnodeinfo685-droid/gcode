
from typing import List
from matplotlib.textpath import TextPath
from ...entities.models import Point, Path, TextGeometry
from ...entities.interfaces import FontService

class MatplotlibFontService(FontService):
    """Implementación del FontService utilizando Matplotlib para vectorizar texto."""
    def get_geometry(self, text: str, size: float) -> TextGeometry:
        # Crea un path vectorial usando las fuentes del sistema/matplotlib
        matplotlib_path = TextPath((0, 0), text, size=size)
        vertices = matplotlib_path.vertices
        codes = matplotlib_path.codes

        paths: List[Path] = []
        current_path = Path()

        for vertex, code in zip(vertices, codes):
            # Matplotlib asigna códigos a los movimientos:
            # 1 = MOVETO (Iniciar nueva línea), 2 = LINETO (Continuar línea), 79 = CLOSEPOLY
            if code == 1: 
                if not current_path.is_empty:
                    paths.append(current_path)
                current_path = Path()
                current_path.add_point(Point(vertex[0], vertex[1]))
            elif code == 2:
                current_path.add_point(Point(vertex[0], vertex[1]))
            elif code == 79:
                if not current_path.is_empty:
                    # Cerrar el polígono repitiendo el primer punto si es necesario
                    current_path.add_point(current_path.points[0])
                    paths.append(current_path)
                current_path = Path()

        if not current_path.is_empty:
            paths.append(current_path)

        return TextGeometry(text, paths)
