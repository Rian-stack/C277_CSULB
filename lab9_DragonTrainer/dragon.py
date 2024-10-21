import entity
import random
import abc

class Dragon(entity.Entity):
    '''
    Dragon Class (dragon.py) – abstract class – inherits from Entity
        1. __init__(self, name, max_hp, num_sp) – call super’s init, then set _special_attacks.
        2. decrement_special_attacks(self) – subtract 1 from _special_attacks. If the value
        becomes negative, then reset it to 0.
        3. basic_attack(self, opponent) – tail attack – the hero takes a random amount of
        damage in the range 3-7. Return a string with the description of the attack and the
        damage dealt to the hero.
        4. special_attack(self, opponent) - call decrement special attacks. This method
        will be overridden in the subclasses.
        5. __str__(self) – use super to get the __str__ from the entity class, then concatenate on
        the number of special attacks remaining.
    '''
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp)
        self._special_attacks = num_sp
    
    def decrement_special_attacks(self):
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self._special_attacks = 0
    
    def basic_attack(self, opponent):
        damage = random.randint(3, 7)
        opponent.take_damage(damage)
        return f"{self.name} attacks with a TAIL WHIP for {damage} damage."
    
    @abc.abstractmethod
    def special_attack(self, opponent):
        self.decrement_special_attacks()
    
    def __str__(self):
        return super().__str__() + f" Special Attacks: {self._special_attacks}"
