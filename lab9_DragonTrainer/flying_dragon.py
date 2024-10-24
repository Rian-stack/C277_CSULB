import dragon
import flying
import random

class FlyingDragon(dragon.Dragon, flying.Flying):
  """
Subclass of class Dragon, and using Mixins class Flying to implement special attack. This class is used for one of the dragon player fight with.
  
  Attributes:
      _name (string): name of dragon. inherited from class                             Dragon                           
      _hp (int): hp of dragon. inherited from class Dragon
      _max_hp (int): maximum hp of dragon. inherit from class Dragon
      _special_attacks(int): Number represent how many times  dragon can use special attack. inherit from class Dragon

  """
  
  def __init__(self,name,max_hp,num_sp):
    super().__init__(name,max_hp,num_sp)
    
  def special_attack(self, opponent):
    """
    ramdomly call one special attack from Mixins class Flying

    Return:
          string that describes special attack, and damege that opponent took.
    """
    if random.randint(0,1) == 0:
     return  self.swoop(opponent)

    else:
      return self.windblast(opponent)