import random

class Fire:
  """
  Mixins class used for class Feredragon and FlyingFireDragon  to have special attack.

  """
  def fireblast(self, opponent):
    """
    do special attack if dragon has number(least 1) of remaining special_attack. opponent takes random damage between 5-9

    Return:
           string that describes special attack, and damege that opponent took
    """
    if self._special_attacks > 0:
      self._special_attacks = self._special_attacks - 1
      damege = opponent.take_damege(random.randint(5,9))
      return f"{self._name} fireblast the {opponent._name} for {damege} damege!"
    else:
      return f"{self._name} failed fireblast,,,,"
      
  def fireball(self, opponent):
    """
    do special attack if dragon has number(least 1) of remaining special_attack. opponent takes random damage between 4-8

    Return:
           string that describes special attack, and damege that opponent took
    """
    if self._special_attacks > 0:
      self._special_attacks = self._special_attacks - 1
      damege = opponent.take_damege(random.randint(4,8))
      return f"{self.name} fireball the {opponent._name} for {damege} damege!"
    else:
      return f"{self.name} failed fireball,,,,"
    