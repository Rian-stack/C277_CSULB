import door
import random

class LockedDoor(door.Door):
  def __init__(self):
    self.solution = random.randint(1,self.get_menu_max())
  def examine_door(self):
    return "A locked door.Look around, the key is hidden nearby."

  def menu_options(self):
    return "1. Look under the mat.\n2. Look underthe flower pot.\n3. Look underthe fake rock."

  def get_menu_max(self):
    return (3)

  def attempt(self, option):
    if option == 1:
      self.user_input = 1
      return "You Look under the mat."
    elif option == 2:
      self.user_input = 2
      return "You Look underthe flower pot"
    else:
      self.user_input = 3
      return "You Look under the fake rock."
  def is_unlocked(self):
    if self.solution == self.user_input:
      return True
    else:
      return False

  def clue(self):
    if not self.is_unlocked():
      return "Look somewhere else."

  def success(self):
    if self.is_unlocked():
      return "You successfull unlocked locked door!!"
    else:
      return ""