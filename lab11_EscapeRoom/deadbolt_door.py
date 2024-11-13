import door
import random

class DeadboltDoor:
  def __init__(self):
    self._sec_toggle = random.randint(0,1)
    self._fir_toggle = random.randint(0,1)

  def examine_door(self):
    return "A double deadbolt door. Both need to be unlocked to open the door, but you can’t tell by looking at them if they’re locked or unlocked."

  def menu_options(self):
    return "1. Toggle bolt 1\n2. Toggle bolt 2"

  def get_menu_max(self):
    return 2

  def attempt(self, option):
    
    if option == 1:
      if not self._fir_toggle:
        self._fir_toggle = random.randint(0,1)
      return "You toggle the first bolt "
      
    else:
      if not self._sec_toggle:
        self._sec_toggle = random.randint(0,1)
      return "You toggle the second bolt "
      
  def is_unlocked(self):
    if self._fir_toggle and self._sec_toggle:
      
      return True
    else:
      return False

  def clue(self):
    if not self.is_unlocked():
      if not self._fir_toggle and not self._sec_toggle:
        return "You jiggle the door... it's completely locked."
      else:
        return "You jiggle the door... it seems like one of the bolts is unlocked"


  def success(self):
    if self.is_unlocked():
      return "You unlocked both deadbolts and opened the door"
    else:
      return ""