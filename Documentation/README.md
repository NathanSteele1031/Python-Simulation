# Documentation Index

Documentation for all program files in the Python-Simulation project, generated 2026-07-26.

| Module | File | Description |
|---|---|---|
| [main.md](main.md) | `main.py` | Program entry point. |
| [map.md](map.md) | `Map/map.py` | `Map` class — the grid of tiles that makes up the world. |
| [tile.md](tile.md) | `Map/tile.py` | `Tile` class — a single grid cell that holds `WorldObject`s. |
| [world_object.md](world_object.md) | `Map/world_object.py` | `WorldObject` base class for anything that can occupy a tile. |
| [plant.md](plant.md) | `Plants/plant.py` | `Plant` class — a `WorldObject` subclass with growth/aging behavior. |
| [plant_manager.md](plant_manager.md) | `Plants/plant_manager.py` | `PlantManager` — static helpers for updating and seeding plants across the map. |
| [data_assets.md](data_assets.md) | `DataAssets/Plants/*.json` | Format of the JSON data files that back `Plant.load_asset`. |

## Project layout

```
main.py                     Entry point
Map/
  __init__.py                (empty)
  map.py                     Map class
  tile.py                    Tile class
  world_object.py             WorldObject base class
Plants/
  __init__.py                (empty)
  plant.py                   Plant class (WorldObject subclass)
  plant_manager.py            PlantManager static helpers
DataAssets/
  Plants/
    grass.json                Data asset for the Grass plant
```

## Known issues

Several bugs found during review are tracked separately in [../Bugs](../Bugs) rather than in this documentation. See that folder for details before relying on `PlantManager.spread_seeds` or `Plant.grown`.
