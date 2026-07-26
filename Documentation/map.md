# `Map/map.py`

Defines `Map`, which owns the full grid of [`Tile`](tile.md)s that make up the simulated world.

## Class: `Map`

### Instance variables

| Name | Type | Description |
|---|---|---|
| `width` | `int` | Width (and height) of the square map. |
| `tiles` | `list[Tile]` | Flattened 1D list of `Tile` instances, `width * width` long. A tile at grid coordinates `(x, y)` lives at `tiles[x + y * width]`. |

### Constructor

#### `__init__(width: int)`

Stores `width`, initializes `tiles` as an empty list, then calls `__set_tiles__()` to populate it with `width * width` empty `Tile` instances.

### Methods

#### `__set_tiles__()`

Private helper that appends `width * width` new `Tile()` instances to `self.tiles`.

> Note: named with leading/trailing double underscores, which conventionally denotes a Python "dunder"/magic method. A single leading underscore (`_set_tiles`) would be the more idiomatic name for a private helper — see [../Bugs](../Bugs).

#### `add_object(index: int, given_object: WorldObject)`

Adds `given_object` to `tiles[index]` via `Tile.add_object`.

- Raises `TypeError` if `given_object` is not a `WorldObject`, or if `index` is not an `int`.

#### `remove_object(index: int, given_object: WorldObject)`

Removes `given_object` from `tiles[index]` via `Tile.remove_object`.

- Raises `TypeError` if `given_object` is not a `WorldObject`, or if `index` is not an `int`.

#### `show()`

Prints the whole map to stdout, row by row: for each row `y` and column `x`, prints `tiles[x + y*width].show()` (see [`Tile.show`](tile.md)), with no separator between columns and a newline after each row.

## Grid indexing

Because `tiles` is a flat list representing a 2D grid, neighbor calculations look like:

- Up: `index - width`
- Down: `index + width`
- Left: `index - 1`
- Right: `index + 1`

None of `Map`'s own methods perform this neighbor math or bounds-check it — `PlantManager.spread_seeds` does (see [plant_manager.md](plant_manager.md)), and currently does so incorrectly for edge tiles (out-of-range/wrap-around indices). See [../Bugs](../Bugs) for details.

## Usage

```python
from Map.map import Map

m = Map(5)      # creates a 5x5 grid of empty Tiles
m.show()        # prints the (currently empty) grid
```
