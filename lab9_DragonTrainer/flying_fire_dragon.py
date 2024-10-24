import dragon
import fire
import flying
import random

class FlyingFireDragon(dragon.Dragon, fire.Fire, flying.Flying):
  """
  Subclass of class Dragon, and using Mixins class Fire and Flying to implement four of special attack. This class is used for one of the dragon player fight with.
  
  Attributes:
      _name (string): name of dragon. inherited from class Dragon                           
      _hp (int): hp of dragon. inherited from class Dragon
      _max_hp (int): maximum hp of dragon. inherit from class Dragon
      _special_attacks(int): Number represent how many times  dragon can use special attack. inherit from class Dragon

  """
  
  def __init__(self,name,max_hp,num_sp):
    super().__init__(name,max_hp,num_sp)
  def special_attack(self, opponent):
    """
    ramdomly call one special attack from Mixins class Flying and Fire

    Return:
          return string from called function, that describes special attack, and damege that opponent took.
    """

    random_int = random.randint(0,3)
    if random_int == 0:
      return self.swoop(opponent)
    elif random_int == 1:
      return self.windblast(opponent)
    elif random_int == 2:
      return self.fireblast(opponent)
    else:
      return self.fireball(opponent)


