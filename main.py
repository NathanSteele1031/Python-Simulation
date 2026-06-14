from Map.map import Map
from Plants.plant import Plant
from Plants.plant_viewer import PlantViewer
from Plants.plant_manager import PlantManager

MAP_WIDTH = 5

def plant_viewer_action(given_input, given_plant_viewer):
    if given_input == " ":
        pass
    if given_input == "w":
        given_plant_viewer.move_up(MAP_WIDTH)
    if given_input == "s":
        given_plant_viewer.move_down(MAP_WIDTH)
    if given_input == "a":
        given_plant_viewer.move_left(MAP_WIDTH)
    if given_input == "d":
        given_plant_viewer.move_right(MAP_WIDTH)

def main():
    global_map = Map(MAP_WIDTH)
    plant_viewer = PlantViewer()

    while True:
        plant_viewer.show(global_map)
        user_input = input("Use space to progress and wasd to move the cursor: ")
        plant_viewer_action(user_input, plant_viewer)

if __name__ == "__main__":
    main()