import sys
from pathlib import Path

# Añade la carpeta src al path para las importaciones
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
