from Map.world_object import WorldObject

class Plant(WorldObject):
    def __init__(self, name: str, seed: bool):
        super().__init__(name)
        self.age = 0
        self.seed = seed
    
    def age_up(self):
        self.age += 1
    
    def grown(self):
        if self.seed and self.age == 5:
            self.seed = not self.seed