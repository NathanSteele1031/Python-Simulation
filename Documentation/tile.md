# `Map/tile.py`

Defines `Tile`, a single cell of the `Map` grid that holds `WorldObject` instances, and the `TILE_MEANING` lookup table used to render tiles as text symbols.

## Module-level constant: `TILE_MEANING`

```python
TILE_MEANING = {
        "priority": ["Water", "Tree", "Grass"],
        "tiletypes" : {
            "Empty" : ' ',
            "Grass" : ',',
            "Tree" : 'T',
            "Water" : '~'
        }
    }
```

- `"priority"`: an ordered list of object names. When a tile contains multiple named objects, the first name in this list that's present determines which symbol is shown.
- `"tiletypes"`: maps an object name (or `"Empty"`) to the single-character symbol printed for it.

Note: this table is independent of the symbols loaded per-plant from `DataAssets/Plants/*.json` (see [data_assets.md](data_assets.md)/[plant.md](plant.md)) — `Tile.show` uses `TILE_MEANING`, while `Plant.show` uses the plant's own `seed_symbol`/`adult_symbol`.

## Class: `Tile`

### Instance variables

| Name | Type | Description |
|---|---|---|
| `objects` | `list[WorldObject]` | All `WorldObject` instances currently on this tile. |
| `object_names` | `list[str]` | Deduplicated list of the `name`s of objects on this tile. |

### Constructor

#### `__init__()`

Initializes `objects` and `object_names` as empty lists.

### Methods

#### `add_object(given_object: WorldObject)`

Appends `given_object` to `objects` and calls `add_object_name(given_object.name)` to record its name.

- Raises `TypeError` if `given_object` is not a `WorldObject`.

#### `add_object_name(given_name: str)`

Appends `given_name` to `object_names` if it isn't already present (keeps the list deduplicated).

- Raises `TypeError` if `given_name` is not a `str`.

#### `remove_object(given_object: WorldObject)`

Removes `given_object` from `objects`. If no remaining object in `objects` shares that name (checked via `object_name_exsist`), the name is also removed from `object_names`.

- Raises `TypeError` if `given_object` is not a `WorldObject`.
- Raises `ValueError` (from `list.remove`) if `given_object` is not actually in `objects`.

#### `object_name_exsist(given_name: str) -> bool`

Returns `True` if any object currently in `objects` has `name == given_name`.

> Note: method name is misspelled (`exsist` instead of `exists`) — kept as-is here to match the current source; see [../Bugs](../Bugs).

#### `show() -> str`

Returns the display symbol for this tile:
1. Walks `TILE_MEANING["priority"]` in order and returns the symbol for the first name found in `object_names`.
2. If none of the priority names are present, returns the `"Empty"` symbol (`' '`).

#### `has_plants() -> bool`

Returns `True` if any object in `objects` is an instance of `Plant` (imported from [`Plants.plant`](plant.md)).

## Usage

Tiles are created and owned by [`Map`](map.md) (one per grid cell). Code should generally go through `Map.add_object` / `Map.remove_object` rather than calling `Tile` methods directly, so that the map can validate the tile index.
