import os
import re

ROOT = r"Z:\\code\\dcs-retribution"

CUSTOM_DIR = os.path.join(ROOT, "resources", "customized_payloads")


def load_task_map() -> dict[int, str]:
    id_map: dict[int, str] = {}
    with open(r"Z:\\code\\pydcs\\dcs\\task.py", encoding="utf-8") as f:
        data = f.read()
    for m in re.finditer(r"class\s+(\w+)\(MainTask\):\s*\n\s*id\s*=\s*(\d+)", data):
        id_map[int(m.group(2))] = m.group(1)
    return id_map


def load_weapon_map() -> dict[str, str]:
    clsid_to_name: dict[str, str] = {}
    with open(r"Z:\\code\\pydcs\\dcs\\weapons_data.py", encoding="utf-8") as f:
        wdata = f.read()
    for m in re.finditer(
        r"=\s*\{\"clsid\":\s*\"([^\"]+)\",\s*\"name\":\s*\"([^\"]+)\"",
        wdata,
    ):
        clsid_to_name[m.group(1)] = m.group(2)
    return clsid_to_name


def classify_weapon(name: str) -> set[str]:
    name_u = name.upper()
    types: set[str] = set()
    if "AAM" in name_u or "AA-" in name_u or "AIM-" in name_u:
        types.add("AAM")
    if "ARM" in name_u or "HARM" in name_u or "ANTI-RADIATION" in name_u:
        types.add("ARM")
    if "ASM" in name_u or "AGM" in name_u or "AIR-TO-GROUND" in name_u:
        types.add("ASM")
    if any(x in name_u for x in ["BOMB", "GBU", "KAB", "MK-", "FAB"]):
        types.add("BOMB")
    if "ROCKET" in name_u:
        types.add("ROCKET")
    if "CLUSTER" in name_u:
        types.add("BOMB")
    return types


def parse_payloads(text: str) -> list[dict]:
    payloads = []

    start_pattern = re.compile(r"\[\d+\]\s*=\s*\{")
    for match in start_pattern.finditer(text):
        start = match.end() - 1  # position at '{'
        brace_count = 0
        in_string = False
        escape = False
        end = None
        for idx in range(start, len(text)):
            ch = text[idx]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
                continue

            if ch == '"':
                in_string = True
                continue

            if ch == "{":
                brace_count += 1
            elif ch == "}":
                brace_count -= 1
                if brace_count == 0:
                    end = idx
                    break

        if end is None:
            continue

        block = text[start + 1 : end]
        name_m = re.search(r"\[\"name\"\]\s*=\s*\"([^\"]+)\"", block)
        if not name_m:
            name_m = re.search(r"\[\"displayName\"\]\s*=\s*\"([^\"]+)\"", block)
        name = name_m.group(1) if name_m else None
        tasks_match = re.search(r"\[\"tasks\"\]\s*=\s*\{(.*?)\}\s*,", block, re.S)
        tasks = (
            [
                int(x)
                for x in re.findall(r"\[(?:\d+)\]\s*=\s*(\d+)", tasks_match.group(1))
            ]
            if tasks_match
            else []
        )
        clsids = re.findall(r"\[\"CLSID\"\]\s*=\s*\"([^\"]+)\"", block)
        payloads.append({"name": name, "tasks": tasks, "clsids": clsids})
    return payloads


def required_weapons_for_task(task_key: str) -> set[str] | None:
    # Return None for tasks where weapon requirements are not applicable.
    if task_key in {
        "AEWC",
        "TRANSPORT",
        "REFUELING",
        "FERRY",
        "AIR_ASSAULT",
        "PRETENSE_CARGO",
        "RECOVERY",
    }:
        return None

    if task_key in {"TARCAP", "BARCAP", "INTERCEPTION", "ESCORT", "SWEEP"}:
        return {"AAM"}

    if task_key in {"SEAD", "DEAD", "SEAD_ESCORT", "SEAD_SWEEP"}:
        return {"ARM"}

    if task_key in {
        "CAS",
        "STRIKE",
        "ANTISHIP",
        "BAI",
        "OCA_RUNWAY",
        "OCA_AIRCRAFT",
        "ARMED_RECON",
    }:
        return {"ASM", "BOMB", "ROCKET"}

    return None


def parse_flight_types() -> list[tuple[str, str]]:
    path = os.path.join(ROOT, "game", "ato", "flighttype.py")
    text = open(path, encoding="utf-8").read()
    entries = []
    for match in re.finditer(r"^\s*([A-Z0-9_]+)\s*=\s*\"([^\"]+)\"", text, re.M):
        entries.append((match.group(1), match.group(2)))
    return entries


def default_loadout_names_for(task_key: str, task_value: str) -> list[str]:
    # prefer_liberation_payloads default is False in this script.
    loadout_names = {
        key: [f"Retribution {val}", f"Liberation {val}"]
        for key, val in parse_flight_types()
    }
    legacy_names = {
        "TARCAP": ("CAP HEAVY", "CAP", "Retribution BARCAP", "Liberation BARCAP"),
        "BARCAP": ("CAP HEAVY", "CAP", "Retribution TARCAP", "Liberation TARCAP"),
        "CAS": ("CAS MAVERICK F", "CAS"),
        "STRIKE": ("STRIKE",),
        "ANTISHIP": ("ANTISHIP",),
        "DEAD": ("DEAD",),
        "SEAD": ("SEAD",),
        "BAI": ("BAI",),
        "OCA_RUNWAY": ("RUNWAY_ATTACK", "RUNWAY_STRIKE"),
        "OCA_AIRCRAFT": ("OCA",),
    }
    for flight_type, names in legacy_names.items():
        loadout_names[flight_type].extend(names)

    # A SEAD escort typically does not need a different loadout than a regular SEAD flight.
    loadout_names["SEAD_ESCORT"].extend(loadout_names["SEAD"])
    loadout_names["SEAD_SWEEP"].extend(loadout_names["SEAD_ESCORT"])
    # Sweep and escort can fall back to TARCAP.
    loadout_names["ESCORT"].extend(loadout_names["TARCAP"])
    loadout_names["SWEEP"].extend(loadout_names["TARCAP"])
    # Intercept can fall back to BARCAP.
    loadout_names["INTERCEPTION"].extend(loadout_names["BARCAP"])
    # OCA/Aircraft falls back to BAI, which falls back to CAS.
    loadout_names["BAI"].extend(loadout_names["CAS"])
    loadout_names["ARMED_RECON"].extend(loadout_names["CAS"])
    loadout_names["OCA_AIRCRAFT"].extend(loadout_names["BAI"])
    # DEAD also falls back to BAI.
    loadout_names["DEAD"].extend(loadout_names["BAI"])
    # OCA/Runway falls back to Strike
    loadout_names["OCA_RUNWAY"].extend(loadout_names["STRIKE"])

    return loadout_names[task_key]


def select_default_payload(
    payloads_by_name: dict[str, dict], task_key: str, task_value: str
) -> dict | None:
    for name in default_loadout_names_for(task_key, task_value):
        payload = payloads_by_name.get(name)
        if payload is not None:
            return payload
    return None


def task_relevant_for_aircraft(aircraft_name: str, task_key: str) -> bool:
    name = aircraft_name.upper()

    transport_fixedwing = [
        "C-",
        "AN-",
        "IL-76",
        "IL-78",
        "KC-",
        "E-3",
        "E-2",
        "A-50",
        "C-17",
        "HERCULES",
        "RQ-",
        "MQ-",
    ]
    aewc = ["E-3", "E-2", "A-50", "EC-121", "AWACS"]
    tanker = ["IL-78", "KC-", "KDC", "S-3B"]
    transport_helo = ["CH-47", "CH-46", "UH-60", "UH-1", "MI-8", "MI-26"]
    attack_helo = ["AH-", "MI-24", "MI-28", "KA-50", "KA-52", "OH-58", "SA342"]
    bomber = ["B-", "B_", "TU-", "TU_", "H-6", "B2", "B-52", "B-1", "B-21"]
    attack_fixedwing = [
        "A-10",
        "A-6",
        "A-7",
        "AJS37",
        "SU-25",
        "SU-24",
        "SU-17",
        "SU-22",
        "MIG-27",
        "F-117",
        "TORNADO IDS",
        "TORNADO GR4",
    ]

    def has_any(tokens: list[str]) -> bool:
        return any(t in name for t in tokens)

    if has_any(aewc):
        return task_key in {"AEWC", "FERRY"}

    if has_any(tanker):
        return task_key in {"REFUELING", "FERRY"}

    if has_any(transport_fixedwing):
        return task_key in {
            "TRANSPORT",
            "PRETENSE_CARGO",
            "RECOVERY",
            "FERRY",
            "REFUELING",
        }

    if has_any(transport_helo):
        return task_key in {
            "TRANSPORT",
            "AIR_ASSAULT",
            "PRETENSE_CARGO",
            "RECOVERY",
            "FERRY",
        }

    if has_any(attack_helo):
        return task_key in {
            "CAS",
            "BAI",
            "ARMED_RECON",
            "STRIKE",
            "OCA_AIRCRAFT",
            "FERRY",
        }

    if has_any(bomber) or has_any(attack_fixedwing):
        return task_key in {
            "CAS",
            "STRIKE",
            "SEAD",
            "DEAD",
            "ANTISHIP",
            "BAI",
            "OCA_RUNWAY",
            "OCA_AIRCRAFT",
            "ARMED_RECON",
            "FERRY",
        }

    # Default: allow all combat tasks and ferry.
    return task_key not in {
        "TRANSPORT",
        "PRETENSE_CARGO",
        "AEWC",
        "REFUELING",
        "AIR_ASSAULT",
    }


def main() -> None:
    clsid_to_name = load_weapon_map()
    issues_by_file: dict[str, list[dict]] = {}
    summary_counts = {
        "no_default_payload": 0,
        "task_rejection": 0,
        "no_weapons": 0,
    }

    for fname in sorted(os.listdir(CUSTOM_DIR)):
        if not fname.lower().endswith(".lua"):
            continue
        path = os.path.join(CUSTOM_DIR, fname)
        text = open(path, encoding="utf-8").read()
        payloads = parse_payloads(text)
        unit_type_match = re.search(r"\[\"unitType\"\]\s*=\s*\"([^\"]+)\"", text)
        unit_type = (
            unit_type_match.group(1) if unit_type_match else fname.replace(".lua", "")
        )
        payloads_by_name = {p["name"]: p for p in payloads if p["name"]}
        file_issues: list[dict] = []

        for task_key, task_value in parse_flight_types():
            if not task_relevant_for_aircraft(unit_type, task_key):
                continue
            payload = select_default_payload(payloads_by_name, task_key, task_value)
            if payload is None:
                summary_counts["no_default_payload"] += 1
                file_issues.append(
                    {
                        "type": "no_default_payload",
                        "task_key": task_key,
                        "task_value": task_value,
                    }
                )
                continue

            weapon_types: set[str] = set()
            for clsid in payload["clsids"]:
                wname = clsid_to_name.get(clsid)
                if wname:
                    weapon_types |= classify_weapon(wname)

            if not weapon_types:
                summary_counts["no_weapons"] += 1
                file_issues.append(
                    {
                        "type": "no_weapons",
                        "task_key": task_key,
                        "task_value": task_value,
                        "payload": payload["name"],
                    }
                )

            required = required_weapons_for_task(task_key)
            if required is not None and not (weapon_types & required):
                summary_counts["task_rejection"] += 1
                file_issues.append(
                    {
                        "type": "task_rejection",
                        "task_key": task_key,
                        "task_value": task_value,
                        "payload": payload["name"],
                        "required": sorted(list(required)),
                        "weapons": sorted(list(weapon_types)),
                    }
                )

        if file_issues:
            issues_by_file[fname] = file_issues

    out_path = os.path.join(ROOT, "CUSTOMIZED_PAYLOADS_REVIEW.md")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# Customized Payloads Review\n\n")
        out.write("## Summary\n\n")
        out.write(
            f"- Tasks with no default payload: {summary_counts['no_default_payload']}\n"
        )
        out.write(
            f"- Payloads missing any weapons (possible AI rejection): {summary_counts['no_weapons']}\n"
        )
        out.write(
            f"- Task-based AI rejection risks (missing required weapon class): {summary_counts['task_rejection']}\n\n"
        )

        out.write("## Per-file findings\n\n")
        for fname, issues in sorted(issues_by_file.items()):
            out.write(f"### {fname}\n\n")
            for issue in issues:
                if issue["type"] == "no_default_payload":
                    out.write(
                        f"- Task **{issue['task_value']}** has no default payload.\n"
                    )
                elif issue["type"] == "no_weapons":
                    out.write(
                        f"- Task **{issue['task_value']}** uses payload **{issue['payload']}** with no recognizable weapons (possible AI rejection).\n"
                    )
                elif issue["type"] == "task_rejection":
                    out.write(
                        f"- Task **{issue['task_value']}** uses payload **{issue['payload']}** but is missing required weapon classes {issue['required']} (detected: {issue['weapons'] or 'none'}).\n"
                    )
            out.write("\n")

    print(out_path)


if __name__ == "__main__":
    main()
