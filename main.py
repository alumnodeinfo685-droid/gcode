"""
Path: main.py
"""

from src.infrastructure.matplotlib.font_service import MatplotlibFontService
from src.infrastructure.gcode.standard_formatter import StandardGCodeFormatter
from src.use_cases.convert_text_to_gcode import ConvertTextToGCodeUseCase
from src.interface_adapter.controllers.cli_controller import CLIController

def main():
    # 1. Configuración de dependencias (Composición de objetos)
    font_service = MatplotlibFontService()
    gcode_formatter = StandardGCodeFormatter()
    
    # Inyectamos las implementaciones en el caso de uso (Inversión de Dependencias)
    use_case = ConvertTextToGCodeUseCase(font_service, gcode_formatter)
    
    # 2. Inicializar el controlador de la interfaz (CLI)
    controller = CLIController(use_case)
    
    # 3. Ejecutar la aplicación
    controller.run()

if __name__ == "__main__":
    main()
