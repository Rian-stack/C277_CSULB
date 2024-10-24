import abc

class Entity(abc.ABC):
  """
  Abstract class for class Hero and Dragon

  Attributes:
      <<get>> _name (string): name of any entity 
      <<get>> _hp (int): hp of entity
      _max_hp (int): maximum hp of entity
  """
  def __init__(self, name, max_hp):
    """
    set attribute, name, max_hp, and initial hp

    Args:
        name and max_hp to set name of entity, and hp & max_hp

    """
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  def take_damege(self, damege):
    """
    calculate damege and hp.

    Args:
        given damege to calculate remaining hp.

    Return: damege(int) that this entity took
    """
    self._hp = self._hp - damege
    if self._hp < 0:
      self._hp = 0
    return damege

  @property
  def name(self):
    return self._name
  @property
  def hp(self):
    return self._hp
  
  def __str__(self):
    """
    return the entity’s name and hp
    
    Return: entity’s name and hp in the format “Name: hp/max_hp”.
    """
    return self._name + ': '  + str(self._hp) + "/" +  str(self._max_hp)

  @abc.abstractmethod
  
  def basic_attack(self, opponent):
    """
    abstract function that need to be overridden
    
    Args:
         opponent that take damege
    Return: 
         entity’s name and hp in the format “Name: hp/max_hp”.
    """
    pass
  
  @abc.abstractmethod
  def special_attack(self, opponent):
    pass
