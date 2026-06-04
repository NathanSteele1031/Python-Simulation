from Plants.plant import Plant
from Map.map import Map
from Map.tile import Tile

class PlantManager:
    @staticmethod
    def update(given_map: Map):
        for selected_tile in given_map.tiles:
            plant_objects = PlantManager.get_plants(selected_tile)
            for selected_plant in plant_objects:
                selected_plant.age_up()
                selected_plant.grown()
    
    @staticmethod
    def get_plants(given_tile: Tile):
        tile_plants = []
        for tile_object in given_tile.objects:
            if isinstance(tile_object, Plant):
                tile_plants.append(tile_object)
        return tile_plants