# Bug Report — 2026-07-27

Findings from a review of the tracked source (`Map/`, `Plants/`).

**Update 2026-07-28:** Bug #1 has been fixed by the user.

---

## 1. ~~Tile display doesn't distinguish a plant's seed vs. adult state~~ — FIXED
**File:** [Map/tile.py:67-76](../Map/tile.py)

`Tile.show()` used to look up a display symbol purely by object name via the module-level `TILE_MEANING` table, so any tile containing a plant named `"Grass"` always showed `,` (`TILE_MEANING["tiletypes"]["Grass"]`) regardless of whether that `Plant` instance was currently a seed or fully grown. `Plant.show()` returns the correct stage-specific symbol (`seed_symbol` vs `adult_symbol`, loaded from the plant's JSON data asset — see [Documentation/plant.md](../Documentation/plant.md)), but nothing in `Tile` or `Map` called it.

**Status:** `Tile.show()` now finds the matching object in `self.objects` by name and delegates to that object's own `.show()`:

```python
def show(self):
    for object_name in TILE_MEANING["priority"]:
        if object_name in self.object_names:
            for given_object in self.objects:
                if given_object.name == object_name:
                    return given_object.show()
    return TILE_MEANING["tiletypes"]["Empty"]
```

Confirmed fixed — a `Grass` plant now shows `.` as a seed and `W` once grown.

Note for later: this now assumes every `WorldObject` that can appear in `TILE_MEANING["priority"]` (currently `Water`, `Tree`, `Grass`) implements its own `.show()`. Only `Plant` does today, so this is fine while grass is the only object in play, but a bare `WorldObject` (e.g. a future `Water`/`Tree` class that doesn't subclass `Plant`) would raise `AttributeError` here since `WorldObject` itself has no `.show()`.

---
