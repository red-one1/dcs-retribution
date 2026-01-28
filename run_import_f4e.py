import importlib,traceback

try:
    importlib.import_module('pydcs_extensions.f4e_expanded_weapons.f4e_expanded_weapons')
    print('IMPORT_OK')
except Exception:
    traceback.print_exc()
