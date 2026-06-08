from Map.tile import Tile, WorldObject

class Map:
    """
    This class is used to keep track of all tiles in the world.

    Instance Variables
    -\n
    width (int) : This represents the width of the square map.
    tiles (list) : A list of Tile instances that make up the map.
    """
    def __init__(self, width: int):
        """
        Sets the given param along with an empty list for the tiles list. Then populates the tiles class with a given width.
        """
        self.width = width
        self.tiles = []
        self.__set_tiles__()

    def __set_tiles__(self):
        """
        Populates the tiles instance variable with empty Tile instances.
        """
        for i in range(self.width*self.width):
            self.tiles.append(Tile())
        
    def add_object(self, index: int, given_object: WorldObject):
        """
        Adds the passed WorldObject to the selected Tile with the tile's add_object function.
        """
        if not isinstance(given_object, WorldObject):
            raise Exception(f"The passed object is not a WorldObject class, '{type(given_object)}'")
        if not isinstance(index, int):
            raise Exception(f"The passed index is not an int class, '{type(index)}'")
        self.tiles[index].add_object(given_object)
        
    def remove_object(self, index: int, given_object: WorldObject):
        """
        Removes the passed WorldObject to the selected Tile with the tile's remove_object function.
        """
        if not isinstance(given_object, WorldObject):
            raise Exception(f"The passed object is not a WorldObject class or a subclass of WorldObject, '{type(given_object)}'")
        if not isinstance(index, int):
            raise Exception(f"The passed index is not an int class, '{type(index)}'")
        self.tiles[index].remove_object(given_object)

    def show(self):
        """
        Goes through all tiles and runs the show function to show all WorldObjects.
        """
        for y in range(self.width):
            for x in range(self.width):
                selected_index = x + (y*self.width)
                print(self.tiles[selected_index].show(), end="")
            print()