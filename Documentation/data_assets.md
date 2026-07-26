# Data Assets — `DataAssets/Plants/*.json`

JSON data files consumed by [`Plant.load_asset`](plant.md). Each file describes one plant type's display symbols and life-cycle timings.

## Location & loading convention

`Plant.load_asset(data_asset_file)` opens `DataAssets/{data_asset_file}` relative to the current working directory. For example, `plant.load_asset("Plants/grass.json")` opens `DataAssets/Plants/grass.json`.

## Schema

| Key | Type | Description |
|---|---|---|
| `name` | `str` | Display name of the plant. Overwrites the `Plant`'s existing `name`. |
| `symbol` | `[str, str]` | Two-element array: `[seed_symbol, adult_symbol]`. Index 0 is used while the plant is a seedling, index 1 once grown. |
| `seed_growth_length` | `int` | Intended age at which the seedling becomes an adult. **Currently not actually used by `Plant.grown()`**, which hardcodes `age == 5` instead — see [../Bugs](../Bugs). |
| `eol_age` | `int` | Age at which `Plant.at_eol()` returns `True` (end of life). |

## Example: `DataAssets/Plants/grass.json`

```json
{
    "name" : "Grass",
    "symbol" : [".", "W"],
    "seed_growth_length" : 5,
    "eol_age" : 20
}
```

This defines a "Grass" plant that displays as `.` while a seedling, `W` once grown, is intended to grow up at age 5 (though this isn't currently wired up), and reaches end of life at age 20.

## Adding a new plant asset

1. Create a new `.json` file under `DataAssets/Plants/` following the schema above.
2. Load it with `Plant("<name>", seed=True).load_asset("Plants/<file>.json")`.

Note: the `symbol` values here are independent of [`Tile`](tile.md)'s `TILE_MEANING` table — `Tile.show()` displays a tile-level symbol (e.g. `,` for any tile containing grass), while `Plant.show()` displays the individual plant's own `seed_symbol`/`adult_symbol` from this file.
