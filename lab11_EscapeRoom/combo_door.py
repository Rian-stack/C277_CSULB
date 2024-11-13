import door
import random

class ComboDoor(door.Door):
  def __init__(self):
    self.solution = random.randint(1,self.get_menu_max())
  def examine_door(self):
    return "A door with acombination lock. You can spin the dial to a number 1-10"

  def menu_options(self):
    return "Enter #1-10: "

  def get_menu_max(self):
    return (10)

  def attempt(self, option):
      self.user_input = option
      return "You entered: " + str(option) 

  def is_unlocked(self):
    if self.solution == self.user_input:
      return True
    else:
      return False

  def clue(self):
    if not self.is_unlocked():
      if self.user_input < self.solution:
         return "Too low"
      elif self.user_input > self.solution:
        return "Too high"
      else:
        raise ValueError("user_input == solution is True, Even thought is_unlocked() is False")
      

  def success(self):
    if self.is_unlocked():
      return "You successfull unlocked conmbo door!!"
    else:
      return ""