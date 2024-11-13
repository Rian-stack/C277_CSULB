import door
import random

class CodeDoor(door.Door):
  def __init__(self):
    self._code = ["O", "O", "O"]
    self._solution_code = [random.choice(["O", "X"]) for _ in range(3)]
    while self._solution_code == self._code:
      self._solution_code = [random.choice(["O", "X"]) for _ in range(3)]
      
    
  def examine_door(self):
    return " door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O‘ There are 3 characters displayed, each one can be toggled to either an 'X' or an 'O'. You can press the key under each character to toggle it."

  def menu_options(self):
    return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3"

  def get_menu_max(self):
    return 3

  def attempt(self, option):

    if option == 1:
      if self._code[0] == "O":
        self._code[0] = "X"
      else:
        self._code[0] = "O"
      return "You toggle the first character." + str(self._code)
    
    elif option == 2:
      if self._code[1] == "O":
        self._code[1] = "X"
      else:
        self._code[1] = "X"
      return "You toggle the first character."
      
    else:
      if self._code[2] == "O":
        self._code[2] = "X"
      else:
        self._code[2] = "X"
      return "You toggle the first character."
      
  def is_unlocked(self):
    if self._code == self._solution_code:
      return True
    else:
      return False

  def clue(self):
    if not self.is_unlocked():
      for i in range(3):
        if self._solution_code[i] == self._code[i]:
          print (f"The {i+1}th  character is correct.")
          return ""

  def success(self):
    if self.is_unlocked():
      return "You entered the correct code and opened the door."
    else:
      return ""