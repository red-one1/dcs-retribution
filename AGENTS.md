Remember to read resources\plugins\base\Moose_commented.lua instead of Moose.lua when trying to understand MOOSE.lua
resources\plugins\base\Moose_commented.lua has detailed comments explaining the functionality of MOOSE.lua and is easier to parse

Make no changes to MOOSE.lua itself, as it is used in production and should remain stable

## Persistency JSON save/load notes (2026-01-27)
- Updated `game/persistency.py` to make JSON saves loadable by embedding a base64 pickle fallback in JSON output. JSON wrapper now contains:
	- `format: "jsonpickle"`
	- `payload`: jsonpickle-flattened data (git-friendly)
	- `pickle`: base64-encoded `pickle.dumps()` of the `Game`
- Load flow for `.json` saves:
	- If JSON has a `pickle` field, it is decoded and loaded via `MigrationUnpickler`.
	- Otherwise it attempts `jsonpickle.decode(..., keys=True)` with a fallback to `keys=False` on unhashable-key errors.
	- Added a sanitizer for unhashable `py/set` entries that converts them to tuples before restoring.
- Added/adjusted jsonpickle handlers:
	- `defaultdict`: now flattens/restores its `items` through jsonpickle context to preserve non-string keys.
	- `ShipUnitType`: includes `py/object` and `variant_id` so key encoding works.
	- `Terrain` handler: serializes terrain objects via pickle to avoid jsonpickle proxy/state issues.

### Findings
- jsonpickle with `keys=True` fails on `defaultdict` with non-string keys unless the handler uses `context.flatten(...)` for items.
- `Terrain` objects cause proxy/state errors during jsonpickle restore; wrapping terrain via pickle avoids this.
- Some legacy JSON saves still fail during jsonpickle restore due to unhashable `Point`/`dict` in sets; the new pickle fallback ensures loadability while retaining a readable `payload`.
