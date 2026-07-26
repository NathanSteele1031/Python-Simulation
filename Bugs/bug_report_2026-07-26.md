# Bug Report — 2026-07-26

Findings from a review of the tracked source (`Map/`, `Plants/`, `DataAssets/`, `main.py`). No fixes have been applied yet.

---

## 1. `spread_seeds` always adds the new plant to the wrong tile
**File:** [Plants/plant_manager.py:44-60](../Plants/plant_manager.py)

`tile_selection` is randomized between 1-4 to pick a neighbor (up/down/left/right), and each branch correctly *checks* the matching neighbor tile (`tile_index - width`, `+ width`, `- 1`, `+ 1`). But all four branches call `.add_object(...)` on `tiles[tile_index - given_map.width]` — the case-1 (up) tile — instead of the tile that was actually checked.

**Effect:** seeds only ever spread upward, regardless of which direction was rolled, and can be added to a tile that was never validated as empty.

```python
if tile_selection == 2:
    if not given_map.tiles[tile_index + given_map.width].has_plants():
        given_map.tiles[tile_index - given_map.width].add_object(Plant(seeding_plant.name, True))  # should be `+ given_map.width`
        break
```
Same issue in the `tile_selection == 3` and `== 4` branches.

---

## 2. `spread_seeds` has no map-edge bounds checking
**File:** [Plants/plant_manager.py:43-60](../Plants/plant_manager.py)

The map is a square grid flattened into a 1D list (`tiles[x + y*width]`). Neighbor math (`tile_index ± width`, `tile_index ± 1`) doesn't check for grid edges:
- `tile_index - width` can go negative for tiles in the top row. Python silently wraps negative indices to the end of the list instead of raising, so this can plant a "neighbor" on the opposite side of the map.
- `tile_index + 1` / `tile_index - 1` can cross row boundaries at the right/left edge (e.g. index at the end of one row treats the start of the next row as its right neighbor).

**Effect:** seeds can spread to unrelated, non-adjacent tiles near map edges.

---

## 3. `spread_seeds` can infinite-loop
**File:** [Plants/plant_manager.py:43](../Plants/plant_manager.py)

The `while True:` loop only `break`s when a randomly chosen neighbor is empty. If all 4 neighbors already have plants, the loop never exits.

**Effect:** hang / unresponsive process once a plant is surrounded on all sides.

---

## 4. `seed_growth_length` is loaded but never used
**File:** [Plants/plant.py:36](../Plants/plant.py), [Plants/plant.py:53](../Plants/plant.py)

`load_asset` reads `seed_growth_length` from the JSON data file and stores it on the instance, but `grown()` hardcodes the threshold instead of reading it back:

```python
def grown(self):
    if self.seed and self.age == 5:   # should reference self.seed_growth_length
        self.seed = not self.seed
```

**Effect:** changing `seed_growth_length` in a data asset (e.g. `DataAssets/Plants/grass.json`) has no effect on actual growth timing — it happens to work for grass only because 5 matches the hardcoded value.

---

## 5. `grown_seedling()` appears to be dead/unclear code
**File:** [Plants/plant.py:39-40](../Plants/plant.py)

```python
def grown_seedling(self):
    return self.age == 10
```

Not called anywhere in the codebase. Its relationship to `grown()` (age 5) and `at_eol()` (`eol_age`, 20 for grass) is unclear — may be leftover from an earlier design.

---

## Minor / non-functional

- **[Map/map.py:20](../Map/map.py)** — `__set_tiles__` uses dunder naming (`__x__`), which is conventionally reserved for Python magic methods. A private helper should use a single leading underscore (`_set_tiles`).
- **[Map/tile.py:58](../Map/tile.py)** — `object_name_exsist` is misspelled (should be `exists`).
- **[Plants/plant.py:47](../Plants/plant.py)** — `load_asset` opens `f"DataAssets/{data_asset_file}"` relative to the current working directory, so it will fail if the script isn't run from the repo root.
- No automated tests exist yet. `spread_seeds` in particular (randomized branching + edge math) is the kind of logic that benefits most from tests, given bugs #1-3 above.
