from Map.world_object import WorldObject

class Plant(WorldObject):
    """
    This is a WorldObject that is for plants.

    Instance Variables
    -\n
    name (str) : The name of the plant.
    age (int) : The age of the plant.
    seed (bool) : This is a flag to see if it's a seedling.
    """
    def __init__(self, name: str, seed: bool):
        """
        Sets the name and seed value passed and sets the age to 0.
        """
        super().__init__(name)
        self.age = 0
        self.seed = seed
    
    def age_up(self):
        """
        Increases the age of the plant by 1.
        """
        self.age += 1
    
    def grown(self):
        """
        A check to see if the plant is a seedling and it able to grow.
        """
        if self.seed and self.age == 5:
            self.seed = not self.seed