from Plants.plant import Plant
from Map.map import Map
from Map.tile import Tile

class PlantManager:
    """
    This is a class with static functions to manage plants.
    """
    @staticmethod
    def update(given_map: Map):
        """
        Goes through all tiles collecting all plants and age up and checks if the plant can grow.
        """
        for selected_tile in given_map.tiles:
            plant_objects = PlantManager.get_plants(selected_tile)
            for selected_plant in plant_objects:
                selected_plant.age_up()
                selected_plant.grown()
    
    @staticmethod
    def get_plants(given_tile: Tile):
        """
        Takes a tile and returns all the plants the tile has. 
        """
        tile_plants = []
        if not isinstance(given_tile, Tile):
            raise TypeError(f"The passed given_tile is not a Tile class, '{type(given_tile)}'")
        for tile_object in given_tile.objects:
            if isinstance(tile_object, Plant):
                tile_plants.append(tile_object)
        return tile_plants
    
    @staticmethod
    def spread_seeds(tile_index: int, seeding_plant: Plant, given_map: Map):
        if not isinstance(tile_index, int):
            raise TypeError(f"The passed value for Tile_index is not an Int class, '{type(tile_index)}'")
        if not isinstance(seeding_plant, Plant):
            raise TypeError(f"The passed value for seeding_plant is a Plant class, '{type(seeding_plant)}'")
        if not isinstance(given_map, Map):
            raise TypeError(f"The passed value for given_map is not a Map class, '{type(given_map)}'")