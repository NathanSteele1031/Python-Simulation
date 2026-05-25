from Map.tile import Tile, WorldObject

class Map:
    
    def __init__(self, width: int):
        self.width = width
        self.tiles = []
        self.__set_tiles__()

    def __set_tiles__(self):
        for i in range(self.width*self.width):
            self.tiles.append(Tile())
        
    def add_object(self, index: int, given_object: WorldObject):
        self.tiles[index].add_object(given_object)
        
    def remove_object(self, index: int, given_object: WorldObject):
        self.tiles[index].remove_object(given_object)

    def show(self):
        for y in range(self.width):
            for x in range(self.width):
                selected_index = x + (y*self.width)
                print(self.tiles[selected_index].show(), end="")
            print()