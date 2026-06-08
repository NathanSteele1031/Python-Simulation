from Map.world_object import WorldObject

TILE_MEANING = {
        "priority": ["Water", "Tree", "Grass"],
        "tiletypes" : {
            "Empty" : ' ',
            "Grass" : ',',
            "Tree" : 'T',
            "Water" : '~'
        }
    }

class Tile:
    """
    This object is to store WorldObject instances. The tile handles showing the objects inside too.\n

    Instance Variables
    -\n
    objects (list) : The WorldObjects that are added to the Tile.
    object_names (list) : This is the names of WorldObjects that are present, no duplicates.
    """
    def __init__(self):
        """
        Generates empty lists for the instance variables: objects and object names.
        """
        self.objects = [] # This will be a list of the object instances.
        self.object_names = [] # This will be a list of names with no duplicates.
    
    def add_object(self, given_object: WorldObject):
        """
        Appends the WorldObject to objects and inserts the name to object names.
        """
        if not isinstance(given_object, WorldObject):
            raise Exception(f"The passed object is not a WorldObject class, '{type(given_object)}'")
        self.objects.append(given_object)
        self.add_object_name(given_object.name)

    def add_object_name(self, given_name: str):
        """
        Checks if the given name is in object_names and if not appends it. 
        """
        if not isinstance(given_name, str):
            raise Exception(f"The passed object is not a String class, '{type(given_name)}'")
        if not given_name in self.object_names:
            self.object_names.append(given_name)
    
    def remove_object(self, given_object: WorldObject):
        """
        Removes the given object from objects
        """
        self.objects.remove(given_object)
        if not self.object_name_exsist(given_object.name):
            self.object_names.remove(given_object.name)

    def object_name_exsist(self, given_name: str):
        """
        This is to check if an object's name exsists in the tile.
        """
        for unchecked_object in self.objects:
            if unchecked_object.name == given_name:
                return True
        return False
    
    def show(self):
        """
        Shows all WorldObjects that are in the tile. There is object priority for certain WorldObjects.
        """
        for object_name in TILE_MEANING["priority"]:
            if object_name in self.object_names:
                return TILE_MEANING["tiletypes"][object_name]
        return TILE_MEANING["tiletypes"]["Empty"]