from __future__ import annotations

from typing import Dict


# Canonical stat names used across the codebase
STAT_NAMES = ("STR", "DEX", "CON", "INT", "WIS", "CHA")


# Built-in race registry (mutable so users can register custom races at runtime)
RACES: Dict[str, Dict[str, int]] = {
    "Human": {s: 1 for s in STAT_NAMES},
    "Elf": {"DEX": 2},
    "Dwarf": {"CON": 2},
}


def list_races() -> list[str]:
    """Return a sorted list of available race names."""
    return sorted(RACES.keys())


def get_race(name: str) -> Dict[str, int] | None:
    """Get the stat bonus mapping for a race by name (case-insensitive)."""
    key = _find_key_case_insensitive(name)
    return RACES.get(key) if key else None


def register_race(name: str, bonuses: Dict[str, int]) -> None:
    """Register or overwrite a race with the provided bonuses.

    Args:
        name: Display name of the race.
        bonuses: Mapping of STAT_NAMES to integer modifiers.
    """
    normalized: Dict[str, int] = {}
    for stat, value in bonuses.items():
        stat_upper = stat.upper()
        if stat_upper in STAT_NAMES and isinstance(value, int):
            normalized[stat_upper] = value
    if not normalized:
        # Ensure at least a no-op race if the input is empty/invalid
        normalized = {}
    RACES[name] = normalized


def apply_race_bonuses(stats: Dict[str, int], race_name: str) -> None:
    """Apply the race bonuses in-place to a stats mapping.

    Unknown race names are ignored (no bonuses applied).
    """
    bonuses = get_race(race_name)
    if not bonuses:
        return
    for stat, delta in bonuses.items():
        stats[stat] = stats.get(stat, 0) + delta


def _find_key_case_insensitive(name: str) -> str | None:
    for k in RACES.keys():
        if k.lower() == name.lower():
            return k
    return None


