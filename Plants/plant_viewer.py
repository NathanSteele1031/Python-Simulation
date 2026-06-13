from Map.map import Map

class PlantViewer:
    def __init__(self):
        self.selected_tile = 0
    
    def show(self, given_map: Map):
        if not isinstance(given_map, Map):
            raise TypeError(f"The passed map value is not a Map class, '{type(given_map)}'")
        for y in range(given_map.width):
            if self.selected_tile == 0 and y == 0:
                print("(", end="")
            else:
                print(" ", end="")
            for x in range(given_map.width):
                print_index = x + (y*given_map.width)
                if self.selected_tile == print_index + 1:
                    print(given_map.tiles[print_index].show(), end="(")
                elif self.selected_tile == print_index:
                    print(given_map.tiles[print_index].show(), end=")")
                else:
                    print(given_map.tiles[print_index].show(), end=" ")
            print()
    
    def move_up(self, map_width: int):
        if self.selected_tile - map_width >= 0:
            self.selected_tile -= map_width
    
    def move_down(self, map_width: int):
        if self.selected_tile + map_width <= map_width ** 2 - 1:
            self.selected_tile += map_width

    def move_left(self, map_width: int):
        if (self.selected_tile - 1) % map_width >= 0 and self.selected_tile % map_width != 0:
            self.selected_tile -= 1
        
    def move_right(self, map_width: int):
        if (self.selected_tile + 1) % map_width != 0:
            self.selected_tile += 1