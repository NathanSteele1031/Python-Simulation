# `Plants/plant_manager.py`

Defines `PlantManager`, a class of `@staticmethod`s for managing [`Plant`](plant.md) objects across a [`Map`](map.md).

## Class: `PlantManager`

All methods are static; the class is never instantiated.

### `update(given_map: Map)`

For every `Tile` in `given_map.tiles`, collects its plants (via `get_plants`) and, for each one, calls `age_up()` then `grown()`.

- This is the per-tick simulation step for plant aging/growth. It does not call `at_eol()` or remove dead plants, and does not call `spread_seeds`.

### `get_plants(given_tile: Tile) -> list[Plant]`

Returns a list of all objects in `given_tile.objects` that are instances of `Plant`.

- Raises `TypeError` if `given_tile` is not a `Tile`.

### `spread_seeds(tile_index: int, seeding_plant: Plant, given_map: Map)`

Attempts to place a new seedling `Plant` (same `name` as `seeding_plant`) on a random empty neighbor of `tile_index`:

1. Validates `tile_index` is `int`, `seeding_plant` is `Plant`, and `given_map` is `Map` (raises `TypeError` otherwise).
2. Loops indefinitely, each iteration picking a random direction 1-4 (up/down/left/right via `random.randint(1, 4)`).
3. If the chosen neighbor tile `has_plants() == False`, adds a new `Plant(seeding_plant.name, True)` and breaks out of the loop.

> **Known issues** (see [../Bugs](../Bugs) for full detail):
> - All four branches add the new plant to the "up" neighbor tile (`tile_index - given_map.width`) regardless of which direction was actually checked/rolled.
> - Neighbor indices (`± width`, `± 1`) are not bounds-checked against map edges, so edge/corner tiles can wrap to unrelated tiles.
> - The `while True` loop has no exit condition if all four neighbors already have plants — it will hang.

## Usage

```python
from Plants.plant_manager import PlantManager

PlantManager.update(global_map)   # ages up and grows all plants on the map
plants_here = PlantManager.get_plants(global_map.tiles[0])
```

`spread_seeds` is not currently called from `update` or anywhere else in the codebase — seeding must be triggered manually.
