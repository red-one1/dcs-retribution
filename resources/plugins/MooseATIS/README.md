# Moose ATIS plugin (Retribution)

## Purpose

This plugin creates MOOSE `ATIS` instances for Retribution airbases by coalition and starts broadcasts automatically.

## How it works

- Iterates all MOOSE airbases using `AIRBASE.GetAllAirbases()`.
- Filters out ships.
- Optionally includes FARPs/helipads.
- Tries to use per-airbase ATC frequencies exported by Retribution (`dcsRetribution.Airbases`) from pydcs terrain radio data, then sets ATIS to `ATC + atisOffsetMHz`.
- Falls back to coalition frequencies when no per-airbase radio data is available.
- Auto-applies available nav aids per airbase from exported beacon data:
	- TACAN (`SetTACAN`)
	- VOR (`SetVOR`)
	- RSBN (`SetRSBN`)
	- ILS (`AddILS`)
	- NDB inner/outer (`AddNDBinner` / `AddNDBouter`)
	- PRMG (`AddPRMG`)
- Uses MOOSE `SetSRS()` for TTS broadcasts (MSRS/SRS path).

## Options

- `enableBlue` / `enableRed`: which coalitions get ATIS.
- `includeFarps`: include helipads/FARPs.
- `blueFrequency` / `redFrequency`: coalition fallback ATIS frequencies in MHz.
- `useFM`: use FM modulation instead of AM.
- `useDcsAirbaseAtcFrequencies`: prefer exported DCS airbase ATC frequencies (`UHF -> VHF high -> VHF low -> HF`) and transmit ATIS at `ATC + atisOffsetMHz`.
- `atisOffsetMHz`: offset added to DCS ATC frequency for ATIS transmission (default `0.5`).
- `setMetricUnits`: enable metric readouts.
- `transmitOnlyWithPlayers`: suppress SRS transmissions when no players are alive.
- `setMapMarks`: enable F10 map marks.
- `reportRunwayLength`: include runway length in reports.
- `reportElevation`: include field elevation in reports.
- `srsPort`: SRS external audio/grpc port.
- `queueUpdateSeconds`: update interval between queue checks (default 90s).
- `startDelaySeconds`: delayed start to let mission systems initialize.
- `debug`: extra logging in `dcs.log`.

## Notes

- This plugin is SRS-centric: it calls `ATIS:SetSRS()` for each created ATIS instance.
- Neutral airbases are skipped.
- If you use FARPs, leave `includeFarps=true` and keep SRS enabled.
- DCS-derived modulation is selected per ATC band (UHF/VHF-high AM, VHF-low/HF FM).
- Nav aids come from the same pydcs/beacon source path already used by Retribution (`beacons` + airport radio data).
