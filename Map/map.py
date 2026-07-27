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
            raise TypeError(f"The passed object is not a WorldObject class, '{type(given_object)}'")
        if not isinstance(index, int):
            raise TypeError(f"The passed index is not an int class, '{type(index)}'")
        self.tiles[index].add_object(given_object)
        
    def remove_object(self, index: int, given_object: WorldObject):
        """
        Removes the passed WorldObject to the selected Tile with the tile's remove_object function.
        """
        if not isinstance(given_object, WorldObject):
            raise TypeError(f"The passed object is not a WorldObject class or a subclass of WorldObject, '{type(given_object)}'")
        if not isinstance(index, int):
            raise TypeError(f"The passed index is not an int class, '{type(index)}'")
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

    def findnear(self, index: int, length: int, object_name: str):
        """
        Searches a square of tiles centered on the given index (including the center tile) for a
        WorldObject with the given name. The square extends `length` tiles in every direction, so
        length=1 searches a 3x3 square, length=2 a 5x5 square, and so on.

        Returns the map index of the first matching tile found (searched row by row, top-left to
        bottom-right), or None if no match is found within the square.
        """
        if not isinstance(index, int):
            raise TypeError(f"The passed index is not an int class, '{type(index)}'")
        if not isinstance(length, int):
            raise TypeError(f"The passed length is not an int class, '{type(length)}'")
        if not isinstance(object_name, str):
            raise TypeError(f"The passed object_name is not a str class, '{type(object_name)}'")

        for dy in range(-length, length + 1):
            for dx in range(-length, length + 1):
                search_index = index + (dy * self.width) + dx
                if self.tiles[search_index].object_name_exsist(object_name):
                    return search_index
        return None