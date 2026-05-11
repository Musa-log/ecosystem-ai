import sys
import os

# Añade la ruta 'src' al sistema para poder importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from employees.base_agent import main

if __name__ == "__main__":
    main()
