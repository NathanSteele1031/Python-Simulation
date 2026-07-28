from Map.map import Map
from Plants.plant import Plant
from Plants.plant_manager import PlantManager

MAP_WIDTH = 5

def main():
    global_map = Map(MAP_WIDTH)

    global_map.show()

if __name__ == "__main__":
    main()