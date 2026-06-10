from Map.map import Map

class PlantViewer:
    def __init__(self):
        self.selected_tile = 0
    
    def show(self, given_map: Map):
        if not isinstance(given_map, Map):
            raise TypeError(f"The passed map value is not a Map class, '{type(given_map)}'")
        print(" ", end="")
        for y in range(given_map.width):
            for x in range(given_map.width):
                print_index = x + (y*self.width)
                