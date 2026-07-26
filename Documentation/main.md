# `main.py`

Program entry point.

## Overview

```python
from Map.map import Map

MAP_WIDTH = 5

def main():
    global_map = Map(MAP_WIDTH)

if __name__ == "__main__":
    main()
```

## Constants

| Name | Value | Description |
|---|---|---|
| `MAP_WIDTH` | `5` | Width (and height) of the square `Map` created by `main()`. |

## Functions

### `main()`

Creates a `Map` of size `MAP_WIDTH x MAP_WIDTH`.

- Currently only constructs the map; it does not add any `WorldObject`s (e.g. `Plant`s), run any simulation ticks (e.g. `PlantManager.update`), or print the map (`Map.show`).
- This is the script's entry point, guarded by the standard `if __name__ == "__main__":` check.

## Notes

- No plants or other objects are added to the map yet, and `PlantManager.update`/`Map.show` are never called, so running this script currently has no visible output. This looks like a work-in-progress scaffold rather than a finished simulation loop.
