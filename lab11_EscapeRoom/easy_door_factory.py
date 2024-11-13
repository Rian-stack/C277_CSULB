import door_factory
import basic_door
import locked_door
import combo_door
import random

class EasyDoorFactory(door_factory.DoorFactory):
  def create_door(self):
    return random.choice([locked_door.LockedDoor(), basic_door.BasicDoor(), combo_door.ComboDoor()])
    
    #ramdomly chose 3 door from easy door