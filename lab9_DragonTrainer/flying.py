import random

class Flying:
  """
  Mixins class used for class Flyingdragon and FlyingFireDragon  to have special attack.
  
  """
  def swoop(self, opponent):   
    """
    do special attack if dragon has number(least 1) of remaining special_attack. opponent takes random damage between 4-8

    Return:
           string that describes special attack, and damege that opponent took
    """
    if self._special_attacks > 0:
      self._special_attacks = self._special_attacks - 1
      damege = opponent.take_damege(random.randint(4,8))
      return f"{self.name} swoop attack the {opponent._name} for {damege} damege!"
    else:
      return f"{self.name} failed Swoop attack,,,"
      
  def windblast(self, opponent):
    """
    do special attack if dragon has number (least 1) of remaining special_attack. opponent takes random damage between 3-7

    Return:
           string that describes special attack, and damege that opponent took
           """
    if self._special_attacks > 0:
      self._special_attacks = self._special_attacks - 1
      damege = opponent.take_damege(random.randint(3,7))
      return f"{self.name} Windblast the {opponent._name} for {damege} damege!"
    else:
      return f"{self.name} failed Windblast attack,,,"
      