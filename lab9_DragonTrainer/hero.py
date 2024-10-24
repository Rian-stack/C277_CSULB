import entity
import random

class Hero(entity.Entity):
  """
  A subclass of the abstract entity class that player play to defeat three dragons. 
  

  Attributes:
      <<get>> _name (string): name of Hero, inherit from class Entity
      <<get>> _hp (int): hp of Hero, inherit from class Entity
      _max_hp (int): maximum hp of Hero inherit from class Entity
  """

  def basic_attack(self, opponent):
    """
    the chose dragon takes a random amount of damage in the
    range 2D6 (1-6 + 1-6)

    Args:
        opponent (entity.Entity): chose dragon takes damege

    Return: tring with the description of the attack and the               damage dealt to the dragon
    """

    damege = opponent.take_damege(random.randint(1, 6) + random.randint(1, 6))
    return f"\n{self._name} slashes the {opponent._name} with their sword for {damege} damege!"
    
  def special_attack(self, opponent):
    """
    the chose the dragon takes a random amount of damage in
the range 1D12 (1-12).

    Args:
        opponent (entity.Entity): chose entity that takes              damege

    Return: string with the description of the attack and the              damage dealt to the dragon
    """
    
    damege = opponent.take_damege(random.randint(1, 12))
    return f"\n{self._name} hits the {opponent._name} with an arrow for {damege} damege!"
    

