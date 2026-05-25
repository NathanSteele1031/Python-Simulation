from tile import Tile

class Map:
    TILE_MEANING = {
        'Grass' : '`',
        'Tree' : 'T',
        'Water' : '~'
    }
    def __init__(self, width):
        self.width = width
        self.tiles = []
        self.__set_tiles__()

    def __set_tiles__(self):
        for i in range(self.width):
            self.tiles.append(Tile())
        
    def add_object(self, index, given_object):
        self.tiles[index].add_object(given_object)
        
        
    def show(self):
        pass