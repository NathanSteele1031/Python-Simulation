from world_object import WorldObject

class Tile:
    def __init__(self):
        self.objects = [] # This will be a list of the object instances.
        self.object_names = [] # This will be a list of names with no duplicates.
    
    def add_object(self, given_object: WorldObject):
        self.objects.append(given_object)
        self.add_object_name(given_object.name)

    def add_object_name(self, given_name: str):
        if not given_name in self.object_names:
            self.object_names.append(given_name)
    
    def remove_object(self, given_object: WorldObject):
        self.objects.remove(given_object)
        if not self.object_name_exsist(given_object.name):
            self.object_names.remove(given_object.name)

    def object_name_exsist(self, given_name: str):
        for unchecked_object in self.objects:
            if unchecked_object.name == given_name:
                return True
        return False
    
    def show(self):
        pass