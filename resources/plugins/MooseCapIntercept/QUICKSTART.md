# Quick Start Guide - Moose CAP Intercept Plugin

## Installation

The plugin is already installed as part of DCS Retribution. No additional installation required.

## Quick Setup (3 Steps)

### 1. Enable the Plugin
1. Open DCS Retribution
2. Go to **Settings** → **Plugins**
3. Check the box next to **"Moose CAP Intercept"**
4. Click **Save**

### 2. Configure Options (Optional)
Default settings work well for most scenarios, but you can adjust:
- **Intercept Range**: 80 NM (how far CAPs will chase bogeys)
- **Max Aspect Angle**: 120° (hot/flanking threshold)
- **Scheduler Interval**: 10 seconds (detection frequency)
- **Debug Mode**: OFF (enable to see what's happening in logs)

### 3. Generate Mission
Create your mission normally with:
- ✅ At least one AWACS/AEW aircraft (E-3, E-2, A-50, etc.)
- ✅ At least one CAP flight (BARCAP or TARCAP)
- ✅ Enemy aircraft (for CAPs to intercept)

**That's it!** The plugin will automatically:
- Discover your AWACS and CAPs when the mission starts
- Monitor for enemy aircraft
- Vector CAPs to intercept hot/flanking threats
- Return CAPs to patrol after intercepts

## Verifying It Works

### In DCS Log (Enable Debug Mode)
Look for these messages in your DCS log file:
```
[CapIntercept] Found AWACS: E-3A_1 (E-3A)
[CapIntercept] Found CAP: F-16C_BARCAP_1
[CapIntercept] Initialization complete
[CapIntercept] F-16C_BARCAP_1 vectored to intercept MiG-29_3
[CapIntercept] F-16C_BARCAP_1 returned to patrol
```

### In DCS Mission
Watch your CAP flights:
- They should patrol normally when no threats
- When enemy aircraft approach, nearest CAP will break off and intercept
- After destroying the bogey, CAP returns to patrol area

## Troubleshooting

### "No CAPs Found" in Log
**Problem**: Plugin can't find your CAP flights  
**Solution**: Ensure CAP group names contain "CAP", "BARCAP", or "TARCAP"

Example good names:
- ✅ "F-16C BARCAP North"
- ✅ "Mirage TARCAP-1"
- ✅ "CAP Flight Alpha"

Example bad names:
- ❌ "F-16C Patrol 1"
- ❌ "Fighter Screen"
- ❌ "Air Defense"

### "No AWACS Found" in Log
**Problem**: Plugin can't find AWACS  
**Solution**: Check your AWACS aircraft type is supported

Supported types (default):
- ✅ E-3A/B/C (US AWACS)
- ✅ E-2C/D (US Carrier AWACS)
- ✅ A-50 (Russian AWACS)
- ✅ Tu-126 (Soviet AWACS)

To add more types, see README.md

### CAPs Not Intercepting
**Common reasons:**

1. **Range too small**: Enemy aircraft outside Intercept Range
   - Solution: Increase Intercept Range in settings

2. **Wrong aspect**: Enemy aircraft flying away (cold aspect)
   - Solution: Increase Max Aspect Angle (try 180° for all aspects)

3. **Already assigned**: Another CAP already assigned to that bogey
   - Solution: This is normal behavior to prevent overkill

4. **CAP busy**: CAP still returning from previous intercept
   - Solution: Wait for CAP to return to patrol status

### CAPs Not Returning to Patrol
**Problem**: CAPs remain at intercept location  
**Solution**: This shouldn't happen, but if it does:
- Check debug log for restoration messages
- Verify Moose is loaded (check for Moose messages early in log)
- Report issue with debug log output

## Advanced Usage

### Multiple CAPs
The plugin supports any number of CAP flights:
- Each bogey gets assigned to nearest available CAP
- Other CAPs continue patrolling
- When a CAP completes intercept, it becomes available again

### Multiple AWACS
All AWACS contribute to a shared detection picture:
- More AWACS = better coverage
- System combines all AWACS radars automatically
- No special configuration needed

### Different Intercept Ranges
Set different ranges for different scenarios:

**Defensive (40-60 NM)**
- CAPs stay close to protected area
- Quick intercepts near friendlies
- Less fuel consumption

**Balanced (70-90 NM) - Default**
- Good balance of coverage and fuel
- Standard doctrine range

**Aggressive (100-120 NM)**
- Push intercepts far forward
- Requires more fuel and tanker support
- Better for offensive operations

### Aspect Angle Settings

**60-90°**: Hot only
- Only intercepts head-on threats
- Very conservative
- Best for defensive CAP

**120°**: Hot + Flanking (Default)
- Intercepts threats heading toward or across
- Good balance
- Standard fighter doctrine

**150-180°**: All aspects
- Intercepts almost any contact
- Very aggressive
- High fuel consumption

## Integration with Retribution

### Flight Planning
- Plan CAP flights normally using Retribution UI
- Plugin doesn't change your waypoints or timing
- CAPs fly their planned routes when idle

### Racetrack Orbits
- Plugin detects when CAPs reach their racetrack
- Original racetrack location saved automatically
- CAPs return here after intercepts

### No Conflicts
The plugin doesn't interfere with:
- Other Retribution plugins
- Your mission planning
- DCS AI tasking
- Radio communications
- Tankers, AWACS, or other support

## Performance

**CPU Impact**: Minimal
- Runs every 10 seconds (configurable)
- Efficient Moose algorithms
- No noticeable performance hit

**Multiplayer**: Compatible
- Runs on server only
- All clients see intercepts
- No additional sync needed

## Tips & Tricks

### Tip 1: Name Your Groups Wisely
Good naming helps you and the plugin:
```
F-16C BARCAP North-1
F-15C TARCAP Alpha
Mirage-2000 CAP West
```

### Tip 2: Position AWACS Well
- Place AWACS to cover CAP patrol areas
- Higher altitude = better radar coverage
- Multiple AWACS for full coverage

### Tip 3: Use Realistic Ranges
- F-15C, F-14: 100+ NM intercept range (long-range missiles)
- F-16C, F/A-18: 60-80 NM intercept range (medium-range missiles)
- MiG-21, F-5: 40-50 NM intercept range (short-range missiles)

### Tip 4: Monitor Fuel
- Intercepts consume fuel
- Plan tanker support for extended ops
- Consider shorter intercept ranges if no tankers

### Tip 5: Debug Mode for Learning
- Enable debug mode on first missions
- Watch what the system does
- Learn optimal settings for your missions
- Disable for production missions

## Getting Help

1. **Check README.md** for detailed documentation
2. **Check IMPLEMENTATION.md** for technical details
3. **Enable Debug Mode** to see what's happening
4. **Check DCS Log** at: `%USERPROFILE%\Saved Games\DCS\Logs\dcs.log`
5. **Report Issues** on DCS Retribution GitHub with log output

## Example Configuration

### Defensive CAP (Blue Team Base Defense)
```
Intercept Range: 60 NM
Max Aspect Angle: 120°
Scheduler Interval: 10 sec
Engage Range: 60 NM
```

### Offensive CAP (Red Zone Operations)
```
Intercept Range: 100 NM
Max Aspect Angle: 150°
Scheduler Interval: 8 sec
Engage Range: 100 NM
```

### Training/Testing
```
Intercept Range: 80 NM
Max Aspect Angle: 180° (all aspects)
Scheduler Interval: 5 sec (fast response)
Debug Mode: ON
```

---

**Need more help?** See README.md for full documentation or IMPLEMENTATION.md for technical details.

**Enjoying the plugin?** Consider contributing to DCS Retribution on GitHub!
