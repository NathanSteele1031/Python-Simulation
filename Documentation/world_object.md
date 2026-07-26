# `Map/world_object.py`

Defines `WorldObject`, the base class for anything that can be placed on a `Tile`.

## Class: `WorldObject`

```python
class WorldObject:
    def __init__(self, name: str):
        self.name = name
```

### Instance variables

| Name | Type | Description |
|---|---|---|
| `name` | `str` | The identifying name of the object (e.g. `"Grass"`). |

### Constructor

#### `__init__(name: str)`

Stores the given `name` on the instance. No other behavior.

## Usage

`WorldObject` is meant to be subclassed. [`Plant`](plant.md) is the only current subclass. `Tile.add_object` / `Tile.remove_object` and `Map.add_object` / `Map.remove_object` all type-check against `WorldObject` (via `isinstance`), so any new kind of object placed on the map (animals, rocks, structures, etc.) should subclass `WorldObject`.
