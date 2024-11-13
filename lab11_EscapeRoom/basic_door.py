import door
import random

class BasicDoor(door.Door):
  def __init__(self):
    self.solution = random.randint(1,self.get_menu_max())
  def examine_door(self):
    return "A basic door. You can either push or pull it to open."
  
  def menu_options(self):
    return "1. Push\n2. Pull\n"
  
  def get_menu_max(self):
    return (2)
  
  def attempt(self, option):
    if option == 1:
      self.user_input = 1
      return "You Pushed the door"
    else:
      self.user_input = 2
      return "You Pulled the door"
    
  def is_unlocked(self):
    if self.solution == self.user_input:
      return True
    else:
      return False
  
  def clue(self):
    if not self.is_unlocked():
      return "Try the other way"
  
  def success(self):
    if self.is_unlocked():
      return "You successfull unlocked basic_door!!!"
    else:
      return ""