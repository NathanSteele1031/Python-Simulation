from Map.world_object import WorldObject
import json

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
        self.seed_symbol = ""
        self.adult_symbol = ""
        self.seed_growth_length = 0
        self.eol_age = 0 #eol is end of life
    
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
        
    def grown_seedling(self):
        return self.age == 10

    def load_asset(self, data_asset_file: str):
        """
        This is to load data asset file from the game folder. \n
        Files will be loaded at DataAssets/"your file path here"
        """
        with open(f"DataAssets/{data_asset_file}", 'r') as file:
            data_asset = json.load(file)

        self.name = data_asset["name"]
        self.seed_symbol = data_asset["symbol"][0]
        self.adult_symbol = data_asset["symbol"][1]
        self.seed_growth_length = data_asset["seed_growth_length"]
        self.eol_age = data_asset["eol_age"]

    def at_eol(self):
        """
        Checks if the plant is at it's end of life.
        """
        return self.age >= self.eol_age
    
    def show(self):
        """
        Returns the symbol of the plant based on if it's a seed. 
        """
        if self.seed:
            return self.seed_symbol
        return self.adult_symbol