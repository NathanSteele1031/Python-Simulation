# `Plants/plant.py`

Defines `Plant`, a [`WorldObject`](world_object.md) subclass representing a growable, aging plant.

## Class: `Plant(WorldObject)`

### Instance variables

| Name | Type | Description |
|---|---|---|
| `name` | `str` | Inherited from `WorldObject`; the plant's name (e.g. `"Grass"`). |
| `age` | `int` | Age in simulation ticks, starts at `0`. |
| `seed` | `bool` | `True` while the plant is a seedling, `False` once grown. |
| `seed_symbol` | `str` | Display symbol used while `seed` is `True`. Set via `load_asset`. |
| `adult_symbol` | `str` | Display symbol used once grown. Set via `load_asset`. |
| `seed_growth_length` | `int` | Age at which the plant should stop being a seedling, per its data asset. Set via `load_asset`. |
| `eol_age` | `int` | "End of life" age. Set via `load_asset`. |

### Constructor

#### `__init__(name: str, seed: bool)`

Calls `WorldObject.__init__(name)`, then sets `age = 0`, `seed = seed`, and initializes `seed_symbol`, `adult_symbol` to `""`, `seed_growth_length` and `eol_age` to `0`. Asset-derived fields are left at these defaults until `load_asset` is called.

### Methods

#### `age_up()`

Increments `age` by 1.

#### `grown()`

If `seed` is `True` and `age == 5`, flips `seed` to `False`.

> Note: the `5` here is hardcoded rather than read from `self.seed_growth_length` (which is loaded from the plant's JSON data asset but otherwise unused). See [../Bugs](../Bugs).

#### `grown_seedling() -> bool`

Returns `age == 10`.

> Note: not called anywhere else in the codebase; its relationship to `grown()` and `at_eol()` is unclear. See [../Bugs](../Bugs).

#### `load_asset(data_asset_file: str)`

Loads a JSON data file from `DataAssets/{data_asset_file}` (path relative to the current working directory) and sets:

- `name` ← `data_asset["name"]`
- `seed_symbol` ← `data_asset["symbol"][0]`
- `adult_symbol` ← `data_asset["symbol"][1]`
- `seed_growth_length` ← `data_asset["seed_growth_length"]`
- `eol_age` ← `data_asset["eol_age"]`

See [data_assets.md](data_assets.md) for the expected JSON schema.

#### `at_eol() -> bool`

Returns `True` if `age >= eol_age`, i.e. the plant has reached end of life.

#### `show() -> str`

Returns `seed_symbol` if `seed` is `True`, otherwise `adult_symbol`.

## Usage

```python
from Plants.plant import Plant

grass = Plant("Grass", seed=True)
grass.load_asset("Plants/grass.json")   # loads DataAssets/Plants/grass.json
grass.age_up()
grass.grown()      # flips seed -> False once age reaches 5
print(grass.show())  # prints seed_symbol or adult_symbol depending on `seed`
```
