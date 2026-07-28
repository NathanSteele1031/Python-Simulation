# Bug Report — 2026-07-27

Findings from a review of the tracked source (`Map/`, `Plants/`).

---

## 1. Tile display doesn't distinguish a plant's seed vs. adult state
**File:** [Map/tile.py:67-74](../Map/tile.py)

`Tile.show()` looks up a display symbol purely by object name via the module-level `TILE_MEANING` table:

```python
def show(self):
    for object_name in TILE_MEANING["priority"]:
        if object_name in self.object_names:
            return TILE_MEANING["tiletypes"][object_name]
    return TILE_MEANING["tiletypes"]["Empty"]
```

Any tile containing a plant named `"Grass"` always shows `,` (`TILE_MEANING["tiletypes"]["Grass"]`), regardless of whether that `Plant` instance is currently a seed or fully grown. `Plant.show()` *does* return the correct stage-specific symbol (`seed_symbol` vs `adult_symbol`, loaded from the plant's JSON data asset — see [Documentation/plant.md](../Documentation/plant.md)), but nothing in `Tile` or `Map` ever calls `Plant.show()`; `Map.show()` only calls `Tile.show()` for each tile.

**Effect:** printing the map (`Map.show()`) never shows a plant transitioning from seedling to adult — the tile's symbol is static for as long as any object with that name occupies it.

**Status:** open, not yet fixed.

---
