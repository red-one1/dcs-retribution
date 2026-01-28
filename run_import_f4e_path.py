import importlib.util, traceback, sys
from pathlib import Path

p = Path(__file__).parent / 'pydcs_extensions' / 'f4e_expanded_weapons' / 'f4e_expanded_weapons.py'
try:
    spec = importlib.util.spec_from_file_location('f4e_expanded_weapons_test', str(p))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    print('IMPORT_OK')
except Exception:
    traceback.print_exc()
