import sys
from pathlib import Path

_here = Path(__file__).parent

_apps_dir = str(_here.parent.parent)
if _apps_dir not in sys.path:
    sys.path.insert(0, _apps_dir)

_minseok_dir = str(_here.parent.parent.parent)
if _minseok_dir not in sys.path:
    sys.path.insert(0, _minseok_dir)
