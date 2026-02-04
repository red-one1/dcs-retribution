# Customized Payloads Review

## Summary

- Tasks with no default payload: 1251
- Payloads missing any weapons (possible AI rejection): 488
- Task-based AI rejection risks (missing required weapon class): 816

## Per-file findings

### A-10A.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.

### A-10C.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Ferry** has no default payload.

### A-10C_2.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Ferry** has no default payload.

### A-20G.lua

- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: ['BOMB']).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: ['BOMB']).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: ['BOMB']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: ['BOMB']).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: ['BOMB']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Recovery** has no default payload.

### A-4E-C.lua

- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### A-7E.lua

- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).

### AH-1W.lua

- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.

### AH-64A.lua

- Task **Ferry** has no default payload.

### AH-64D.lua

- Task **Ferry** has no default payload.

### AH-64D_BLK_II.lua

- Task **Strike** has no default payload.
- Task **Ferry** has no default payload.

### AJS37.lua

- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.

### AV8BNA.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### AWING.lua

- Task **TARCAP** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### B-17G.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### B-1B.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.

### B-21.lua

- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.

### B-52H.lua

- Task **CAS** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### B2_Spirit.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### B_47.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### B_58.lua

- Task **CAS** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **BAI** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.

### Bf-109K-4.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Bronco-OV-10A.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### C-101CC.lua

- Task **Transport** has no default payload.
- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### CH-47Fbl1.lua

- Task **Transport** has no default payload.
- Task **Ferry** has no default payload.
- Task **Air Assault** uses payload **Retribution Air Assault** with no recognizable weapons (possible AI rejection).
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### CH_JAS39C.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### CH_Ka52.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: ['ASM']).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### CH_Ka52K.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: ['ASM']).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### CH_Mi28N.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### CH_Su-27P1M.lua

- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### CH_Tu-160M2.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Runway** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### CORVETTE.lua

- Task **TARCAP** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### EA-18G.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### EA_6B.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### F-117A.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### F-14A-135-GR-Early.lua

- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### F-14A-135-GR.lua

- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### F-14A.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### F-14B.lua

- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### F-15C.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### F-15D.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution Intercept** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution Intercept** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### F-15E.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Recovery** has no default payload.

### F-15ESE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### F-16A MLU.lua

- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### F-16A.lua

- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### F-16C_50.lua

- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM', 'ARM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### F-16D_50.lua

- Task **Recovery** has no default payload.

### F-16D_50_NS.lua

- Task **Recovery** has no default payload.

### F-16D_52.lua

- Task **Recovery** has no default payload.

### F-16D_52_NS.lua

- Task **Recovery** has no default payload.

### F-16D_Barak_30.lua

- Task **Recovery** has no default payload.

### F-16D_Barak_40.lua

- Task **Recovery** has no default payload.

### F-16I.lua

- Task **Recovery** has no default payload.

### F-22A.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Retribution Intercept** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution Intercept** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### F-4E-45MC.lua

- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### F-4E.lua

- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### F-5E-3.lua

- Task **AEW&C** has no default payload.
- Task **Ferry** has no default payload.

### F-5E-3_FC.lua

- Task **AEW&C** has no default payload.
- Task **Ferry** has no default payload.

### F-86F Sabre.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **OCA** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **OCA** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### F-86F_FC.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### F111C.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** has no default payload.
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### F4U-1D.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['BOMB', 'ROCKET']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### FA-18C.lua

- Task **DEAD** uses payload **Liberation DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### FA-18C_hornet.lua

- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Recovery** has no default payload.

### FA-18E.lua

- Task **TARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Recovery** has no default payload.

### FA-18F.lua

- Task **TARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Recovery** has no default payload.

### FAUCON.lua

- Task **TARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### FW-190A8.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### FW-190D9.lua

- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: ['ROCKET']).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: ['ROCKET']).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: ['ROCKET']).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: ['ROCKET']).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: ['ROCKET']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### H-6J.lua

- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.

### HUNTER.lua

- Task **TARCAP** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### Hercules.lua

- Task **Transport** has no default payload.
- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### I-16.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### J-11A.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Recovery** has no default payload.

### JAS39Gripen.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### JAS39Gripen_AG.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** has no default payload.
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** has no default payload.
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **OCA** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **OCA** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### JAS39Gripen_BVR.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### JF-17.lua

- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Recovery** has no default payload.

### Ju-88A4.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** has no default payload.
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### Ka-50.lua

- Task **AEW&C** has no default payload.
- Task **Ferry** has no default payload.

### Ka-50_3.lua

- Task **AEW&C** has no default payload.
- Task **Ferry** has no default payload.

### L-39C.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### L-39ZA.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### M-2000C.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **Recovery** has no default payload.

### MB-339A.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### MQ-9 Reaper.lua

- Task **Transport** has no default payload.
- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### Mi-24P.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Mi-24V.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Mi-28.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Mi-28N.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Mi-8MT.lua

- Task **Transport** has no default payload.
- Task **Ferry** has no default payload.
- Task **Air Assault** uses payload **Retribution Air Assault** with no recognizable weapons (possible AI rejection).
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### MiG-15bis.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Recovery** has no default payload.

### MiG-15bis_FC.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### MiG-19P.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### MiG-21bis.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM', 'ROCKET']).
- Task **DEAD** uses payload **DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM', 'ROCKET']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM', 'ROCKET']).
- Task **Recovery** has no default payload.

### MiG-23MLD.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### MiG-25PD.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-25RBT.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### MiG-27K.lua

- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.

### MiG-29 Fulcrum.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-29A.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-29G.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-29MU2.lua

- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-29S.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-31.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### MiG-31BM.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Escort** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### Mirage 2000-5.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Mirage-F1B.lua

- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Mirage-F1BE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1C-200.lua

- Task **Transport** has no default payload.
- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1CE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1CT.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1EE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1EQ.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1M-CE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### Mirage-F1M-EE.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### MosquitoFBMkVI.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### OH-58D.lua

- Task **Ferry** has no default payload.

### OH-6A.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### OH58D.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: ['ASM']).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### P-47D-30.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### P-47D-30bl1.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### P-47D-40.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Escort** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Recovery** has no default payload.

### P-51D-30-NA.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### P-51D.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### P3C_Orion.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### RQ-1A Predator.lua

- Task **Transport** has no default payload.
- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### Rafale_A_S.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Rafale_B.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Rafale_M.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### S-3B.lua

- Task **Refueling** has no default payload.
- Task **Ferry** has no default payload.

### SA342L.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### SA342M.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### SA342Minigun.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** has no default payload.
- Task **BAI** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### SA342Mistral.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### SH-60B.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### SK-60.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** has no default payload.
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** has no default payload.
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### SpitfireLFMkIX.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### SpitfireLFMkIXCW.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### Su-17M4.lua

- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.

### Su-24M.lua

- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.

### Su-24MU.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Su-25.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).

### Su-25T.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Su-27.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Recovery** has no default payload.

### Su-30.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM', 'ARM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Su-30MKA.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Su-30MKI.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Recovery** has no default payload.

### Su-30MKM.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Su-30SM.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### Su-33.lua

- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM', 'BOMB']).
- Task **Recovery** has no default payload.

### Su-34.lua

- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### Su-57.lua

- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### Su_15.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### Su_15TM.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### TIE.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### TIEB.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM', 'BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### TIE_INTER.lua

- Task **TARCAP** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### Tornado GR4.lua

- Task **Ferry** has no default payload.

### Tornado IDS.lua

- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.

### Tornado_ADV.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### Tu-142.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Runway** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).

### Tu-16.lua

- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### Tu-160.lua

- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **Ferry** has no default payload.

### Tu-22M3.lua

- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### Tu-4K.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **STRIKE** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **STRIKE** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution OCA/Runway** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### Tu-95MS.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** has no default payload.
- Task **OCA/Runway** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### Tu_128M.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### Tu_95K.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** has no default payload.
- Task **OCA/Runway** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.

### UH-1H.lua

- Task **Transport** has no default payload.
- Task **Ferry** has no default payload.
- Task **Air Assault** uses payload **Retribution Air Assault** with no recognizable weapons (possible AI rejection).
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### UH-60L.lua

- Task **Transport** uses payload **Liberation Transport** with no recognizable weapons (possible AI rejection).
- Task **Ferry** uses payload **Liberation Ferry** with no recognizable weapons (possible AI rejection).
- Task **Air Assault** uses payload **Liberation Air Assault** with no recognizable weapons (possible AI rejection).
- Task **Cargo Transport** has no default payload.
- Task **Recovery** has no default payload.

### VSN_A6A.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F100.lua

- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F104C.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### VSN_F104G.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### VSN_F104S.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F104S_AG.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F105D.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Intercept** uses payload **Retribution Intercept** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution Intercept** but is missing required weapon classes ['AAM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution OCA/Aircraft** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F105G.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F106A.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F106B.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F35A.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F35A_AG.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F35B.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F35B_AG.lua

- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Ferry** has no default payload.

### VSN_F35C.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F35C_AG.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'ASM']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F4B.lua

- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### VSN_F4C.lua

- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F4E.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **Ferry** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_F84G.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### VSN_F9F.lua

- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **BAI** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** uses payload **BAI** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### VSN_MirageIIIC.lua

- Task **CAS** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### VSN_MirageIIIC_AG.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### VSN_MirageIIIS.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### VSN_SEM.lua

- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### WingLoong-I.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** has no default payload.
- Task **BAI** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **CAS** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### XWING.lua

- Task **TARCAP** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Liberation BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Liberation BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **Liberation TARCAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Liberation TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### YWING.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['ASM']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **Ferry** has no default payload.
- Task **Recovery** has no default payload.

### Yak_28.lua

- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### a_37_dragonfly.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **BAI** but is missing required weapon classes ['ARM'] (detected: ['AAM', 'BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### naboo_starfighter.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### sh2f.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### tu_22D.lua

- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Ferry** has no default payload.

### tu_22KD.lua

- Task **Anti-ship** uses payload **ANTISHIP** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **ANTISHIP** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **DEAD** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **DEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.

### uh2a.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### uh2b.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### uh2c.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### vwv_a1_skyraider.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **DEAD** uses payload **Retribution DEAD** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** uses payload **Retribution SEAD** with no recognizable weapons (possible AI rejection).
- Task **SEAD Escort** uses payload **Retribution SEAD** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** with no recognizable weapons (possible AI rejection).
- Task **SEAD Sweep** uses payload **Retribution SEAD Sweep** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Armed Recon** uses payload **Retribution Armed Recon** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### vwv_ad4_skyraider.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **CAS** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### vwv_ch46d.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### vwv_ch46d_late.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### vwv_crusader.lua

- Task **CAS** has no default payload.
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **BAI** has no default payload.
- Task **OCA/Runway** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### vwv_crusader_np.lua

- Task **TARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** has no default payload.
- Task **Fighter sweep** uses payload **CAP** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **CAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### vwv_ec-121.lua

- Task **AEW&C** has no default payload.
- Task **Ferry** has no default payload.

### vwv_mig17f.lua

- Task **TARCAP** uses payload **Retribution TARCAP** with no recognizable weapons (possible AI rejection).
- Task **TARCAP** uses payload **Retribution TARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BARCAP** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **BARCAP** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Intercept** uses payload **Retribution BARCAP** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution BARCAP** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: none).
- Task **Escort** uses payload **Retribution Escort** with no recognizable weapons (possible AI rejection).
- Task **Escort** uses payload **Retribution Escort** but is missing required weapon classes ['AAM'] (detected: none).
- Task **BAI** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **BAI** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Fighter sweep** uses payload **Retribution Fighter sweep** with no recognizable weapons (possible AI rejection).
- Task **Fighter sweep** uses payload **Retribution Fighter sweep** but is missing required weapon classes ['AAM'] (detected: none).
- Task **OCA/Aircraft** uses payload **Retribution BAI** with no recognizable weapons (possible AI rejection).
- Task **OCA/Aircraft** uses payload **Retribution BAI** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### vwv_mig21mf.lua

- Task **CAS** uses payload **Retribution CAS** with no recognizable weapons (possible AI rejection).
- Task **CAS** uses payload **Retribution CAS** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['BOMB']).
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: ['AAM']).
- Task **Recovery** has no default payload.

### vwv_o-1.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **Intercept** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** uses payload **Retribution BAI** but is missing required weapon classes ['ARM'] (detected: ['ROCKET']).
- Task **Escort** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Recovery** has no default payload.

### vwv_ra-5.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** uses payload **Retribution Intercept** with no recognizable weapons (possible AI rejection).
- Task **Intercept** uses payload **Retribution Intercept** but is missing required weapon classes ['AAM'] (detected: none).
- Task **Strike** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **Strike** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** uses payload **Retribution Strike** with no recognizable weapons (possible AI rejection).
- Task **OCA/Runway** uses payload **Retribution Strike** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** uses payload **Retribution Armed Recon** with no recognizable weapons (possible AI rejection).
- Task **Armed Recon** uses payload **Retribution Armed Recon** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **Recovery** has no default payload.

### vwv_rf101b.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** has no default payload.
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

### vwv_sh2f.lua

- Task **TARCAP** has no default payload.
- Task **BARCAP** has no default payload.
- Task **CAS** has no default payload.
- Task **Intercept** has no default payload.
- Task **Strike** has no default payload.
- Task **Anti-ship** uses payload **Retribution Anti-ship** with no recognizable weapons (possible AI rejection).
- Task **Anti-ship** uses payload **Retribution Anti-ship** but is missing required weapon classes ['ASM', 'BOMB', 'ROCKET'] (detected: none).
- Task **SEAD** has no default payload.
- Task **DEAD** has no default payload.
- Task **Escort** has no default payload.
- Task **BAI** has no default payload.
- Task **Fighter sweep** has no default payload.
- Task **OCA/Runway** has no default payload.
- Task **OCA/Aircraft** has no default payload.
- Task **SEAD Escort** has no default payload.
- Task **Ferry** has no default payload.
- Task **SEAD Sweep** has no default payload.
- Task **Armed Recon** has no default payload.
- Task **Recovery** has no default payload.

