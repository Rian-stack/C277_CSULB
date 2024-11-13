import door_factory
import deadbolt_door
import code_door
import combo_door
import random

class DifficultDoorFactory(door_factory.DoorFactory):
  def create_door(self):
    return random.choice([code_door.CodeDoor(), deadbolt_door.DeadboltDoor(), combo_door.ComboDoor()])