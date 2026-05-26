from Map.world_object import WorldObject

class Plant(WorldObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.age = 0
    
    def age_up(self):
        self.age += 1