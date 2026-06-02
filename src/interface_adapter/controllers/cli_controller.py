
import os
from datetime import datetime
from ...entities.models import MachineConfig
from ...use_cases.convert_text_to_gcode import ConvertTextToGCodeUseCase

class CLIController:
    """Controlador para la interfaz de línea de comandos."""
    def __init__(self, use_case: ConvertTextToGCodeUseCase):
        self._use_case = use_case

    def run(self):
        print("=== Generador de G-code con Arquitectura Limpia ===")
        
        # 2. Definición de parámetros de entrada de la aplicación
        texto_a_convertir = input("Ingrese texto a convertir a GCODE: ")
        tamaño_letra = 12  # Escala relativa de la tipografía
        
        configuracion_maquina = MachineConfig(
            safe_z=5.0,        # Levanta a 5mm del plano
            work_z=-0.5,       # Graba penetrando 0.5mm el material
            feed_rate_xy=1200, # Velocidad de corte en plano X-Y (mm/min)
            feed_rate_z=300    # Velocidad de entrada en Z (mm/min)
        )
        
        # 3. Ejecución de la lógica de negocio
        try:
            lineas_gcode = self._use_case.execute(
                text=texto_a_convertir, 
                font_size=tamaño_letra, 
                config=configuracion_maquina
            )
            
            # 4. Salida del resultado (Salvar a disco e imprimir muestra)
            os.makedirs("data", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            nombre_archivo = f"{timestamp}.gcode"
            ruta_salida = os.path.join("data", nombre_archivo)
            
            with open(ruta_salida, "w", encoding="utf-8") as archivo:
                archivo.write("\n".join(lineas_gcode))
                
            print(f"\n[Éxito] Archivo generado exitosamente: '{os.path.abspath(ruta_salida)}'")
            
            print("\n--- Muestra de las primeras 25 líneas del código generado ---")
            for linea in lineas_gcode[:25]:
                print(linea)
            print("...")
            
        except ValueError as e:
            print(f"[Error de Validación]: {e}")
        except Exception as e:
            print(f"[Error del Sistema]: Ocurrió un fallo inesperado: {e}")
