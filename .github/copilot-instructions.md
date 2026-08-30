# DCS Retribution – Copilot Architecture Instructions

## Application Overview

DCS Retribution is a **turn-based dynamic campaign manager** for [DCS World](https://www.digitalcombatsimulator.com/).
It is an **external desktop application** (not a DCS mod) that:

1. Manages a persistent campaign state (control points, squadrons, budgets, ground forces).
2. Generates a DCS `.miz` mission file each turn for the player to fly in DCS.
3. Processes post-mission debriefing results to update the campaign state.

It was forked from [DCS Liberation](https://github.com/dcs-liberation/dcs_liberation).
Save files are **not** backward-compatible with Liberation.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Desktop UI | Python 3 + PyQt5 |
| Game/backend | Python 3 (`game/`) |
| Map UI | React + TypeScript (`client/`) |
| Map API server | FastAPI (`game/server/`) |
| Mission generation | [pydcs](https://github.com/pydcs/dcs) (`pydcs_extensions/` for custom units) |
| Save format | Python `pickle` |
| Type checking | mypy |
| Tests | pytest |
| Packaging | PyInstaller (`pyinstaller.spec`) |
| Scripting (in-mission) | Lua (via pydcs + `resources/scripts/`, `resources/plugins/`) |

---

## Top-Level Directory Structure

```
dcs-retribution/
├── client/          # React + TypeScript map UI
├── docs/            # Documentation source
├── game/            # Core Python game engine (see below)
├── pydcs_extensions/# Custom aircraft/unit type definitions for pydcs
├── qt_ui/           # PyQt5 desktop UI widgets and windows
├── resources/       # Static data: campaigns, factions, theaters, units, scripts
├── tests/           # pytest unit tests
└── unshipped_data/  # Unreleased/WIP campaign data
```

---

## Core Architecture: `game/`

The `game/` package is the heart of the application. Key sub-packages:

### Central State (`game/game.py`)

`Game` is the root serialisable object for one campaign save. It owns:

- `game.theater` – a `ConflictTheater` (map + control points)
- `game.blue` / `game.red` – two `Coalition` objects
- `game.settings` – a `Settings` instance
- `game.conditions` – current weather/time-of-day
- `game.turn` – integer turn counter

`Game` is serialised to disk via `pickle` (see `game/persistency.py`).
Save migration is handled by `game/migrator.py` (`Migrator`) and
`game/persistency.py` (`MigrationUnpickler`).
Breaking save-compat increments `MAJOR_VERSION` in `game/version.py`.

---

### Theater (`game/theater/`)

| File | Purpose |
|------|---------|
| `conflicttheater.py` | `ConflictTheater` – terrain + list of `ControlPoint`s, front lines |
| `controlpoint.py` | `ControlPoint` base class + subtypes (Airbase, Carrier, FOB, FARP, OffMap) |
| `frontline.py` | `FrontLine` – border between two adjacent enemy control points |
| `theatergroundobject.py` | `TheaterGroundObject` (TGO) – SAMs, EWRs, factories, ammo depots, etc. |
| `theatergroup.py` | `TheaterGroup` / `TheaterUnit` – units inside a TGO |
| `iadsnetwork/` | Skynet-IADS network: `IadsNetwork`, `SkynetNode`, `IadsRole` |
| `transitnetwork.py` | Road / shipping / airlift connectivity graph for supply routing |
| `theaterloader.py` | Loads per-terrain YAML data (seasonal conditions, daytime map) |
| `start_generator.py` | Initialises a brand-new campaign from a `.miz` + config |

Supported DCS terrains (via pydcs):
Caucasus, Falklands, Persian Gulf, Normandy, Mariana Islands, Nevada (NTTR),
The Channel, Syria, Sinai, Kola, Afghanistan, Iraq, Germany Cold War.

Campaign files live in `resources/theaters/<theater>/` and `resources/campaigns/`.
The campaign format is versioned (`CAMPAIGN_FORMAT_VERSION` in `game/version.py`,
currently `(10, 8)`).

---

### Coalition (`game/coalition.py`)

`Coalition` represents one side (Blue = player, Red = enemy, Neutral = neutral).
Each `Coalition` owns:

- `ato` – `AirTaskingOrder` (all planned flight packages for this turn)
- `air_wing` – `AirWing` (all squadrons + aircraft)
- `armed_forces` – `ArmedForces` (ground force groups)
- `transfers` – `PendingTransfers` (in-transit ground units)
- `transit_network` – `TransitNetwork` (routing graph)
- `_threat_zone` – `ThreatZones` (recomputed on load, not persisted)
- `_navmesh` – `NavMesh` (recomputed on load, not persisted)
- `procurement_requests` – queued `AircraftProcurementRequest`s

---

### Air Tasking Order (`game/ato/`)

| File | Purpose |
|------|---------|
| `airtaaskingorder.py` | `AirTaskingOrder` – ordered list of `Package`s |
| `package.py` | `Package` – a mission package (one or more flights against a single target) |
| `flight.py` | `Flight` – a group of aircraft (from one squadron) assigned a mission |
| `flighttype.py` | `FlightType` enum (TARCAP, BARCAP, CAS, STRIKE, SEAD, DEAD, ESCORT, etc.) |
| `flightplans/` | Per-mission-type waypoint plan generation |
| `flightwaypoint.py` | Individual waypoints with altitude, speed, timing |
| `loadouts.py` | Weapon loadout selection |
| `starttype.py` | `StartType` (Cold/Warm/Runway/Air start) |
| `traveltime.py` | TOT (time-over-target) estimation |

A `Package` has one target (`MissionTarget`) and one or more `Flight`s.
Each `Flight` belongs to a `Squadron` and has a `FlightType`.

---

### Mission Generator (`game/missiongenerator/`)

Converts the current game state into a DCS `.miz` file using pydcs.
`MissionGenerator.generate_miz(output: Path)` is the entry point.

Sub-generators called in sequence:

| Class | Responsibility |
|-------|---------------|
| `EnvironmentGenerator` | Weather, time of day, cloud presets |
| `TgoGenerator` | Ground objects (SAMs, EWRs, factories, ammo depots) |
| `AircraftGenerator` | Aircraft flight groups with DCS AI tasks and waypoints |
| `ConvoyGenerator` | Ground vehicle convoys between control points |
| `CargoShipGenerator` | Naval cargo shipping |
| `FlotGenerator` | Front-line of troops (FLOT) |
| `TriggerGenerator` | DCS triggers (capture zones, win/loss conditions) |
| `LuaGenerator` | Lua data tables for Skynet-IADS, JTAC, plugins |
| `BriefingGenerator` | Mission briefing text |
| `KneeboardGenerator` | Pilot kneeboard pages |
| `DrawingsGenerator` | DCS map drawings |
| `VisualsGenerator` | Visual aids (smoke, markings) |

---

### AI Campaign Commander (`game/commander/`)

The AI planner uses a **Hierarchical Task Network (HTN)** (`game/htn.py`).
The generic HTN framework in `htn.py` provides `WorldState`, `PrimitiveTask`,
`CompoundTask`, and `Planner`.

`TheaterCommander` (per coalition) decomposes high-level goals
(e.g. "capture base X") into concrete flight plan requests:

```
PlanNextAction → (compound)
  ├── Defend → reinforce front, set stance, plan CAS
  ├── Prepare → destroy IADS, plan DEAD/SEAD
  ├── Inhibit → strike factories/logistics
  └── Attack → breakthrough stance, plan CAS support
```

`tasks/` contains both compound and primitive HTN task classes.
`theaterstate.py` holds the mutable `TheaterState` world model used during planning.

---

### Simulation Loop (`game/sim/`)

Used for *pre-mission* simulation (optional "run to first contact" feature)
and for tracking the simulation clock while the `.miz` is being played.

| File | Purpose |
|------|---------|
| `gameloop.py` | `GameLoop` – timer-driven loop; start/pause/run-to-first-contact |
| `missionsimulation.py` | `MissionSimulation` – drives `AircraftSimulation` tick-by-tick |
| `aircraftsimulation.py` | Simulates aircraft positions and combat events |
| `missionresultsprocessor.py` | Applies simulation results to game state |
| `gameupdateevents.py` | Event bus for UI notifications during sim |
| `simspeedsetting.py` | Speed multiplier enum (paused / 1× / 2× / …) |

After the real DCS mission is flown, debriefing is processed by `game/debriefing.py`
which parses the `.log` file written by in-mission Lua scripts.

---

### Procurement & Economy (`game/procurement.py`, `game/income.py`)

- **Income** (`Income`): calculated per turn from controlled bases and alive TGO buildings.
  Rates defined in `game/config.py` (`REWARDS` dict).
- **ProcurementAi**: AI decision logic for buying aircraft, repairing runways,
  and purchasing ground units within the coalition's budget.

---

### Ground Forces (`game/ground_forces/`, `game/transfers.py`)

- `ai_ground_planner.py` – `GroundPlanner`: determines front-line stances and moves
  (Attack / Defend / Breakthrough / etc.).
- `transfers.py` – manages `TransferOrder` objects for moving ground units between
  control points via `Convoy` (road), `CargoShip` (sea), or `Airlift` (air).
  Routing uses `TransitNetwork` (Dijkstra).

---

### Factions (`game/factions/`, `resources/factions/`)

Factions are defined as JSON files in `resources/factions/`.
`FactionLoader` deserialises them into `Faction` dataclass instances.
A `Faction` defines available aircraft, ground units, ships, SAMs,
doctrine (Modern / Cold War / WWII), country, and locales for name generation.

There are 100+ faction definitions covering historical and modern scenarios.

---

### Squadrons (`game/squadrons/`)

| File | Purpose |
|------|---------|
| `airwing.py` | `AirWing` – all squadrons for a coalition at a given game state |
| `squadron.py` | `Squadron` – roster of `Pilot`s, aircraft type, task assignments |
| `pilot.py` | `Pilot` – name, status (Active / On leave / MIA / KIA), experience |
| `squadrondef.py` | `SquadronDef` – template loaded from YAML (name, aircraft, tasks) |
| `squadrondefloader.py` | Loads squadron definition files |

Squadron definitions for campaigns live in `resources/squadrons/`.

---

### Settings (`game/settings/`)

Hierarchical settings system using Python dataclasses with descriptor-based options:
`boolean_option`, `bounded_int_option`, `bounded_float_option`, `choices_option`, etc.
Settings are grouped into pages and sections (Difficulty, Campaign Management,
Campaign Doctrine, Mission Generator, Pretense).
`Settings` is persisted as part of the `Game` pickle.

---

### Pretense Mode (`game/pretense/`)

An alternate, more dynamic campaign mode that generates a self-sustaining
Lua-scripted environment where AI autonomously resupplies and reinforces bases.
Has its own mission generator, TGO generator, trigger generator, and Lua generator.

---

### Plugins (`game/plugins/`, `resources/plugins/`)

`LuaPluginManager` embeds optional Lua scripts into the generated mission:
- **Skynet-IADS** – AI-driven integrated air defence network.
- **JTAC Autolase** (Ciribob) – auto-laser for JTAC targets.
- **Arty Spotter / Call Artillery Script** – ground artillery support.
- Custom plugin `.lua` files from `resources/plugins/`.

---

### Persistence & Migration

| File | Purpose |
|------|---------|
| `game/persistency.py` | `load_game` / `save_game` via `pickle`; `MigrationUnpickler` for class renames |
| `game/migrator.py` | `Migrator` – fixes up loaded `Game` objects from older versions |
| `game/savecompat.py` | `@has_save_compat_for(major)` decorator – ensures old compat code is removed |
| `game/version.py` | `MAJOR_VERSION`, `MINOR_VERSION`, `MICRO_VERSION`, `CAMPAIGN_FORMAT_VERSION` |

A change to `MAJOR_VERSION` signals a save-compatibility break.
`MigrationUnpickler` handles renamed classes; `Migrator` handles structural changes.

---

## Desktop UI: `qt_ui/`

PyQt5-based application shell.

| File/Dir | Purpose |
|----------|---------|
| `main.py` | Application entry point |
| `windows/QLiberationWindow.py` | Main application window |
| `simcontroller.py` | Bridges `GameLoop` with Qt signals/slots |
| `windows/newgame/` | New game wizard |
| `windows/mission/` | Mission planning dialogs |
| `windows/settings/` | Settings dialog |
| `windows/finances/` | Finances / budget dialog |
| `widgets/` | Reusable Qt widget components |
| `models.py` | Qt data models for lists/tables |

---

## Map UI: `client/` + `game/server/`

The interactive campaign map is a React SPA served from the local FastAPI server.

### FastAPI Server (`game/server/`)

`app.py` creates the FastAPI app and includes routers for:
`controlpoints`, `flights`, `frontlines`, `tgos`, `supplyroutes`,
`mapzones`, `navmesh`, `iadsnetwork`, `debuggeometries`, `eventstream`, `waypoints`, `game`, `qt`.

The server runs on port **16880** (default) using `uvicorn`.

### React Client (`client/src/`)

| Dir | Purpose |
|-----|---------|
| `api/` | Auto-generated API client (OpenAPI) |
| `app/` | Redux store / app-level state |
| `components/` | UI components (map layers, dialogs, panels) |
| `hooks/` | Custom React hooks |

The map is rendered with [Leaflet](https://leafletjs.com/).
Real-time updates use server-sent events (`eventstream` endpoint).

---

## Turn Flow (High-Level Lifecycle)

```
1. New Turn
   ├── AI TheaterCommander plans packages (HTN) → updates Coalition.ato
   ├── ProcurementAi buys units and repairs runways
   └── Ground forces advance / fight

2. Mission Planning (human + AI)
   ├── Player reviews/edits ATO in Qt UI
   └── Waypoints solved, TOT estimated

3. Mission Generation
   └── MissionGenerator.generate_miz() → writes .miz file

4. Player flies mission in DCS World

5. Debriefing
   ├── Debriefing.from_json() parses mission result log
   └── MissionResultsProcessor updates game state
       ├── Aircraft losses recorded to Squadron rosters
       ├── Ground unit losses applied
       ├── Control point capture/liberation processed
       └── Budget updated (income + salvage)

6. Turn End
   └── game.pass_turn() → increments turn, regenerates conditions, transfers complete
```

---

## Key Data Files in `resources/`

| Path | Contents |
|------|---------|
| `resources/factions/*.json` | Faction definitions (100+ factions) |
| `resources/theaters/<name>/` | Per-theater YAML configs, landmaps |
| `resources/campaigns/` | Campaign `.miz` + `.yaml` files |
| `resources/squadrons/` | Squadron definition YAML files |
| `resources/units/aircraft/*.yaml` | Per-aircraft task weights and loadout configs |
| `resources/payloads/` | Weapon payload definitions |
| `resources/plugins/` | Bundled Lua plugins (Skynet, JTAC, etc.) |
| `resources/scripts/` | In-mission Lua utility scripts (MIST) |
| `resources/layouts/` | TGO layout templates |

---

## pydcs Extensions (`pydcs_extensions/`)

Adds aircraft and unit types not in the base pydcs library, one sub-package per
aircraft/mod (e.g. `f4/`, `su57/`, `highdigitsams/`, `irondome/`).
Also provides `pylon_injector.py` and `weapon_injector.py` for augmenting
existing pydcs aircraft definitions with additional weapons.

---

## Testing

```bash
pytest                   # run all tests
pytest tests/            # same
```

Test modules are in `tests/` and also inline in `tests/dcs/`, `tests/flightplan/`,
`tests/missiongenerator/`, `tests/theater/`.
Significant test files: `test_factions.py`, `test_radios.py`, `test_sidc.py`,
`test_tacan.py`, `test_daytimemap.py`.

Type checking: `mypy` (configured in `mypy.ini`).
Pre-commit hooks: `.pre-commit-config.yaml` (black, isort, flake8, mypy).

---

## Important Conventions

- `game/` uses `from __future__ import annotations` and forward-reference TYPE_CHECKING guards heavily to avoid circular imports.
- Volatile (recomputable) state on `Game` / `Coalition` is prefixed with `_` and re-initialised in `on_load()` to keep pickle saves minimal.
- `@has_save_compat_for(MAJOR_VERSION)` must annotate any method that handles old save data; it raises at startup if the major version does not match.
- `FlightType` enum values are persisted to save files – never rename or remove them without a migration.
- Campaign YAML format version is tracked in `CAMPAIGN_FORMAT_VERSION` tuple; bump the minor component for additive changes, major for breaking changes.
- All monetary values (budget, income) use `float` denominated in an abstract "credits" unit. `game/config.py` defines building income rates; `game/income.py` computes per-turn totals.
- The `player` field (`Player.BLUE` / `Player.RED`) identifies a coalition side throughout the codebase; `coalition_id` maps Blue→2, Red→1 (matching DCS coalition IDs).
