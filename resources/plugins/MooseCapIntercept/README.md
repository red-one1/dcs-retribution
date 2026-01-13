# Moose CAP Intercept Plugin

## Overview

The Moose CAP Intercept plugin provides automated interception capabilities for BARCAP/TARCAP flights in DCS Retribution missions. It uses Moose's detection and tasking systems to dynamically vector CAP flights to intercept hot/flanking enemy aircraft detected by AWACS/AEW platforms.

## Features

- **Auto-discovery**: Automatically discovers AWACS/AEW groups and CAP flights from the mission
- **Smart intercept vectoring**: Only vectors CAPs to bogeys with hot/flanking aspect (≤120°) within range (≤80nm by default)
- **Assignment tracking**: Prevents multiple CAPs from being assigned to the same bogey
- **Route restoration**: Returns CAPs to their original patrol after intercept completion
- **Configurable parameters**: Adjust ranges, aspects, and timing via plugin UI

## Configuration

The plugin can be configured through the DCS Retribution UI with the following options:

| Option | Default | Range | Description |
|--------|---------|-------|-------------|
| Intercept Range | 80 NM | 20-150 NM | Maximum range from CAP to bogey for intercept consideration |
| Max Aspect Angle | 120° | 60-180° | Maximum aspect angle for hot/flanking determination |
| Scheduler Interval | 10 sec | 5-60 sec | How often to check for new intercept opportunities |
| Engage Range | 80 NM | 40-150 NM | ROE engage range for intercepting CAPs |
| Debug Mode | false | - | Enable detailed logging to DCS log file |

## How It Works

### 1. Auto-Discovery Phase (Mission Start + 5s)

- **AWACS Discovery**: Scans all aircraft groups for AWACS/AEW types (E-3, E-2, A-50, Tu-126, etc.)
- **CAP Discovery**: Identifies friendly CAP flights by checking group names for "CAP", "BARCAP", or "TARCAP"
- **Route Extraction**: Stores each CAP's current position as racetrack reference for later restoration

### 2. Detection and Intercept Loop (Every ~10s)

1. Moose DETECTION_AREAS polls AWACS radars for enemy aircraft detections
2. For each detected bogey:
   - Check if already assigned to a CAP (skip if yes)
   - Calculate range from nearest available CAP
   - Calculate aspect angle (bogey heading vs line to CAP)
   - If range ≤ configured max AND aspect ≤ configured max:
     - Vector nearest CAP to intercept using AUFTRAG:NewINTERCEPT
     - Set ROE to Weapon Free, Alarm State to Red, priority to 1
     - Track assignment to prevent double-tasking

### 3. Restoration (When Bogey Dies or Intercept Completes)

- Detects when assigned bogey is destroyed
- Creates new CAP mission at original racetrack location
- Returns CAP to patrol status for future intercepts

## Extending AWACS Types

To add support for additional AWACS/AEW aircraft types, edit the `AWACS_TYPES` table in `Plugin_CapIntercept.lua`:

```lua
local AWACS_TYPES = {
    -- NATO/US AWACS
    "E-3A",
    "E-2C",
    "E-2D",
    
    -- Russian/Soviet AWACS
    "A-50",
    "Tu-126",
    
    -- Add your custom types here
    "KJ-2000",  -- Chinese AWACS
    "E-767",    -- Japanese AWACS
    -- etc.
}
```

The detection uses string matching, so partial type names work (e.g., "E-3" matches "E-3A", "E-3B", etc.).

## Adjusting Thresholds

All thresholds can be adjusted via the plugin configuration UI without editing code:

- **Intercept Range**: Increase for earlier intercepts, decrease for tighter CAP coverage
- **Max Aspect Angle**: 
  - 90° = Hot/Flanking only (bogey heading toward or across CAP)
  - 120° = Default (includes some beam aspects)
  - 180° = All aspects (intercept regardless of bogey heading)
- **Scheduler Interval**: Lower values provide faster response but higher CPU load
- **Engage Range**: Should typically match or exceed Intercept Range

## Compatibility

### Requirements

- DCS Retribution mission generator
- Moose framework (included in base plugin)
- AWACS/AEW aircraft in the mission
- CAP flights with "CAP", "BARCAP", or "TARCAP" in group name

### Moose Version

Compatible with Moose version included in DCS Retribution base plugin. The plugin uses:

- `SET_GROUP` for AWACS grouping
- `DETECTION_AREAS` for radar detection
- `FLIGHTGROUP` for CAP flight control
- `AUFTRAG` for mission tasking
- `COORDINATE` for position calculations

### Integration Notes

- Plugin is loaded after Moose via `configurationWorkOrders`
- Starts 5 seconds after mission begins to allow groups to spawn
- Does not interfere with existing Retribution waypoints or tasks
- CAPs fly their original routes when idle (no changes unless intercept triggered)

## Troubleshooting

### No Intercepts Happening

1. **Check AWACS**: Enable Debug Mode and check DCS log for "Found AWACS" messages
2. **Check CAPs**: Look for "Found CAP" messages in log
3. **Check Range**: Bogeys may be outside configured Intercept Range
4. **Check Aspect**: Bogeys may have cold/beam aspect (flying away from CAPs)
5. **Check Detection**: AWACS may not have radar contact on bogeys

### CAPs Not Returning to Patrol

- CAP restoration uses a simple coordinate-based approach
- If issues occur, CAPs may remain in intercept mode
- Consider increasing Scheduler Interval if system is too aggressive

### Performance Issues

- Reduce Scheduler Interval (increase time between checks)
- Limit number of CAP flights in mission
- Ensure Debug Mode is disabled for production missions

## Debug Mode

Enable Debug Mode in plugin options to see detailed logging:

```
[CapIntercept] Discovering AWACS groups...
[CapIntercept]   Found AWACS: E-3A_1 (E-3A)
[CapIntercept] Discovering CAP flights...
[CapIntercept]   Found CAP: F-16C_BARCAP_1
[CapIntercept] Processing 3 detections
[CapIntercept]   Intercept conditions MET: Range=45.2NM, Aspect=65.3°
[CapIntercept] F-16C_BARCAP_1 vectored to intercept MiG-29_3
[CapIntercept]   Bogey MiG-29_3 destroyed, releasing CAP
[CapIntercept] Restoring F-16C_BARCAP_1 to patrol
```

## Known Limitations

1. **Route Persistence**: Current implementation stores position-based racetrack anchors rather than full route data. CAPs may not return to exact original waypoints.

2. **Task Detection**: CAP flight discovery relies on group name heuristics ("CAP", "BARCAP", "TARCAP") rather than direct DCS task inspection due to mission scripting API limitations.

3. **Moose AUFTRAG**: The plugin uses Moose's AUFTRAG system which requires specific Moose version compatibility. Test thoroughly with your Moose version.

4. **Coalition Hardcoded**: Currently scans only Blue coalition for CAPs. Edit `coalition.side.BLUE` in code if Red CAPs needed.

5. **Single AWACS Set**: All AWACS share a single detection set. Individual AWACS coverage zones not modeled.

## Future Enhancements

Possible improvements for future versions:

- [ ] Full route persistence using mission file parsing
- [ ] Per-AWACS detection zones
- [ ] Coalition configuration option
- [ ] Direct DCS task inspection when API allows
- [ ] Integration with Retribution flight planning UI
- [ ] Tanker coordination for extended intercepts
- [ ] Multi-CAP coordination for same bogey
- [ ] Intercept success/failure metrics

## Credits

Developed for DCS Retribution dynamic campaign system.
Uses Moose framework by FlightControl et al.

## License

Part of DCS Retribution project. See main repository for license.
