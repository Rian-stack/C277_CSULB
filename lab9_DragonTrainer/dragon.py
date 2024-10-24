import entity
import random

class Dragon(entity.Entity):
  """
  A subclass of the abstract entity class. This is base class used to create three defferent dragon Class. 


  Attributes:
      _name (string): name of dragon inherited from class                           Entity
      _hp (int): hp of dragon inherited from class Entity
      _max_hp (int): maximum hp of dragon inherit from class                          Entity
      _special_attacks(int): Number represent how many times dragon can use special attack. 
      
  """

  def __init__(self, name, max_hp, num_sp):
    """
    call super to set attributes; name, max_hp, initial hp, and then set new attribute _sepcial_attacks

    Args:
        name and max_hp to set attributes by calling super's           init. num_sp is used to set _special_attacks
    """
    super().__init__(name, max_hp)
    self._special_attacks = num_sp

  def decrement_special_attacks(self):
    """
    subtract 1 from _special_attacks when dragon uses special      attack. If the value becomes negative, then reset it to 0

    Args:
        name and max_hp to set attributes by calling super's           init. num_sp is used to set _special_attacks
    """
    self._special_attacks = self._special_attacks - 1
    if self._special_attacks < 0:
      self._special_attacks = 0

  def basic_attack(self, opponent):
    damege = opponent.take_damege(random.randint(3, 7))
    return f"{self._name} smashes you with its tail for {damege} damege!"

  def __str__(self):
    """
    use super to get the __str__ from the entity class, then       concatenate on the number of special attacks remaining.
 
    Return: entity’s name, hp, number of remaining special attack in the format “Name: hp/max_hp/special_attacks"
    """

    return super().__str__() + "\nSpecial Attack remaining: " + str(
        self._special_attacks)

  @property
  def special_attacks(self):
    return self._special
