class Person:
  def __init__(self):
    self.hunger = 0
    self.health = 100
    self.right_hand = None
    self.left_hand = None

  def eat(self):
    # Check if the item in any hands is a food item

    #Then decrease hunger if it is food
    pass

  def pickup_item(self, item):
    # Check if either hands are empty and set hand values to item value
    pass

  def drop(self, hand: str):
    # Returns the item that is in the selected hand from hand perameter
    pass

  def move(self, direction: str):
    # Moves self object in the world map. (needs to figure out how map works)
    pass

  def AI_actions(self):
    # Perform actions based on needs. (work on after functional person class and implamented to main game.)
    pass
